# Warm Paper Light

A light Obsidian theme with neutral cream surfaces, dark text and restrained colours.

Warm Paper Light supports the Light base colour scheme and requires Obsidian 1.15.1 or later. The [theme manifest](manifest.json) records the current source version.

## Preview

![Light mode](screenshot.png)

## Install manually

1. Download `manifest.json` and `theme.css` from [latest published release](https://github.com/tutivsoft-com/obsidian-theme-warm-paper-light/releases/latest).
2. Put both files in `.obsidian/themes/Warm Paper Light/` in your vault.
3. Open **Settings > Appearance** and select **Warm Paper Light**. Set the base colour scheme to **Light**.

## Run the source checks

Run the tests from the repository root with Python 3 and the CSS parser dependencies.

```sh
python -m pip install cssselect2 tinycss2
python -B -m unittest discover -s tests
```

See the [desktop UI verification](docs/testing/obsidian-ui-2026-11-24/README.md) for the test results and screenshots.

See the [original design plan](PLAN.md). [MIT license](LICENSE).
