import json
import unittest
from pathlib import Path
from xml.etree import ElementTree

from cssselect2 import ElementWrapper, Matcher, compile_selector_list
from tinycss2 import parse_declaration_list, parse_stylesheet, serialize


ROOT = Path(__file__).resolve().parents[1]


def build_matcher():
    matcher = Matcher()
    stylesheet = (ROOT / "theme.css").read_text(encoding="utf-8")
    for rule in parse_stylesheet(stylesheet, skip_comments=True, skip_whitespace=True):
        if rule.type != "qualified-rule":
            raise ValueError(f"Unexpected CSS at line {rule.source_line}: {rule.type}")
        declarations = {}
        for declaration in parse_declaration_list(
            rule.content, skip_comments=True, skip_whitespace=True
        ):
            if declaration.type != "declaration":
                raise ValueError(
                    f"Invalid CSS declaration at line {declaration.source_line}"
                )
            declarations[declaration.name] = serialize(declaration.value).strip()
        # The static selector engine cannot receive keyboard focus. Mark the
        # focused fixture nodes so it can still check the selector cascade.
        selectors = serialize(rule.prelude).replace(":focus-visible", "[data-focus]")
        for selector in compile_selector_list(selectors):
            matcher.add_selector(selector, declarations)
    return matcher


def fixture(body_classes, mobile_wrapper=""):
    document = ElementTree.fromstring(
        f"""<body class="{body_classes}" id="body">
          <main class="{mobile_wrapper}">
            <div class="workspace-leaf-content">
              <section class="markdown-source-view mod-cm6">
                <div class="cm-contentContainer">
                  <div class="cm-content" id="editor" data-focus="">
                    <span class="list-bullet" id="source-bullet"/>
                  </div>
                </div>
              </section>
              <button id="unfocused"/>
            </div>
            <section class="markdown-rendered">
              <span class="list-bullet" id="reading-bullet"/>
            </section>
          </main>
          <div class="menu" id="menu"><button id="menu-button" data-focus=""/></div>
          <div class="modal" id="modal"><button id="modal-button" data-focus=""/></div>
        </body>"""
    )
    root = ElementWrapper.from_html_root(document)
    return {element.id: element for element in root.iter_subtree() if element.id}


class ThemeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matcher = build_matcher()

    def styles(self, element, pseudo=None):
        declarations = {}
        for _, _, pseudo_element, rule in self.matcher.match(element):
            if pseudo_element == pseudo:
                declarations.update(rule)
        return declarations

    def test_light_theme_styles_surfaces_and_bullets(self):
        light = fixture("theme-light")
        palette = self.styles(light["body"])
        self.assertEqual(palette["--background-primary"], "#f8f3e7")
        self.assertEqual(palette["--text-normal"], "#282217")
        for surface in ("menu", "modal"):
            with self.subTest(surface=surface):
                self.assertEqual(
                    self.styles(light[surface])["background-color"],
                    "var(--background-primary)",
                )
        for bullet in ("source-bullet", "reading-bullet"):
            with self.subTest(bullet=bullet):
                self.assertEqual(
                    self.styles(light[bullet], "after")["background-color"],
                    "var(--text-muted)",
                )

    def test_light_focus_outline_and_mobile_padding(self):
        desktop = fixture("theme-light")
        for focused in ("editor", "menu-button", "modal-button"):
            with self.subTest(focused=focused):
                styles = self.styles(desktop[focused])
                self.assertEqual(styles["outline"], "2px solid var(--text-accent)")
                self.assertEqual(styles["outline-offset"], "-2px")
        self.assertNotIn("outline", self.styles(desktop["unfocused"]))
        self.assertNotIn("padding-inline", self.styles(desktop["editor"]))
        for light in (fixture("theme-light is-mobile"), fixture("theme-light", "is-mobile")):
            self.assertEqual(self.styles(light["editor"])["padding-inline"], "8px")

    def test_dark_and_unset_schemes_keep_host_styles(self):
        for body_classes in ("theme-dark", "theme-dark is-mobile", "is-mobile"):
            for name, element in fixture(body_classes).items():
                for pseudo in (None, "after"):
                    with self.subTest(body_classes=body_classes, name=name, pseudo=pseudo):
                        self.assertEqual(self.styles(element, pseudo), {})

    def test_installation_files_and_manifest(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "Warm Paper Light")
        for field in ("version", "minAppVersion"):
            self.assertRegex(manifest[field], r"^\d+\.\d+\.\d+$")
        self.assertTrue(manifest["author"].strip())
        self.assertTrue((ROOT / "LICENSE").is_file())
        self.assertEqual((ROOT / "screenshot.png").read_bytes()[:8], b"\x89PNG\r\n\x1a\n")


if __name__ == "__main__":
    unittest.main()
