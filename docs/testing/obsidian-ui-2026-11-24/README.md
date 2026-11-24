# Warm Paper Light desktop UI verification

Warm Paper Light 3.7.2 was tested in Obsidian 1.15.1 on Windows on 2026-11-24. The theme files were installed in a separate Obsidian profile and a local vault containing synthetic notes, a Canvas and a Base.

## Fixes verified

| Reproduced in 3.7.1 | Result in 3.7.2 |
| --- | --- |
| The inset keyboard outline met the first text column in Live Preview. It crossed the first glyph of unindented lines. | Light mode gives the editor text an 8 px inset in Live Preview and Source mode. The 2 px focus outline remains visible. |
| The Workshop note callout used a bright turquoise title against its pale green fill. | Callout titles use the theme's dark text colour. The callout fill and icon keep their type colours. |
| Appearance dropdowns and secondary buttons had white fills on the cream settings page. | Resting controls use the paper colour. Hover uses the tinted interface colour. |

## UI checks

| Check | Result |
| --- | --- |
| Reading view | Checked text and two heading colours, internal and external links, properties, bullets, tasks, the callout, table, code syntax and highlight. |
| Navigation | Followed an internal link and checked the Backlinks, Outgoing links, Tags, All properties and Outline panes. |
| Live Preview | Verified the keyboard outline, text inset and bullets. Checked a task and undid the change. |
| Source mode | Selected text, replaced it by typing, undid the edit and found text in the note. |
| File context menu | Opened by right-click, moved keyboard selection and closed with Escape. |
| Command palette | Searched for the Reading view command and checked the selected result and dialog colours. |
| Quick switcher and bookmark | Opened Reference Sheet from the keyboard. Checked keyboard focus and form colours in the bookmark dialog, then saved the bookmark. |
| Vault search | Checked results and an empty search, opened a result and verified the focused input colours. |
| Graph view | Opened the rendered graph and checked the graph controls and inherited palette. |
| Canvas | Opened three demo cards with two connections, fit the canvas and selected a card. |
| Bases | Opened the demo notes table and exercised the sort and filter controls. |
| Appearance | Checked the selected Light scheme and Warm Paper Light theme in the settings window, and verified dropdown and button backgrounds. |
| Dark fallback | Compared 41 palette properties and representative headings and bullets with Obsidian's default Dark theme. Switched back to Light and verified the cream palette returned. |
| Mobile selector | Checked the 8 px Light inset and the Dark fallback using the mobile class in the desktop renderer. |

The four source tests passed. This run covered the Windows desktop renderer. Native mobile clients and system-driven appearance changes are outside the verification scope.

## Screenshots

The ten captures came from the Obsidian renderer and contain only the sample vault.

1. [Reading view](01-reading-view.png)
2. [Live Preview keyboard focus](02-live-preview-focus.png)
3. [Source mode text selection](03-source-selection.png)
4. [File context menu](04-file-context-menu.png)
5. [Command palette](05-command-palette.png)
6. [Vault search results](06-vault-search.png)
7. [Canvas with cards and connectors](07-canvas.png)
8. [Bases notes table](08-bases.png)
9. [Appearance settings](09-appearance-settings.png)
10. [Obsidian Dark fallback](10-dark-host-fallback.png)
