# Warm Paper Light design plan

A light Obsidian theme with neutral cream surfaces, dark text and restrained colours.

This plan records the original 13 November 2026 proposal, before implementation and publication. See the [README](README.md) for current installation and compatibility information.

Search keywords: Obsidian theme, light mode, cream, warm paper, readable notes.

## Who this is for

People who want a light theme without stark white or a strong yellow cast.

## User need and evidence

Light-theme users describe pure white as harsh and some yellow palettes as too yellow. They want a balanced alternative.

- [Light-theme preferences and cream versus white](https://www.reddit.com/r/ObsidianMD/comments/1tdwk3a/whats_everyones_favorite_light_theme_setup_in/)

The Reddit discussion informed the original design proposal.

## Planned appearance and features

- Use a neutral cream background with gentle warm panel variations.
- Keep body text dark and crisp, with enough contrast for small interface text.
- Use restrained ink-blue, muted green and warm brown accents.
- Give headings, links, callouts and selections clear but quiet styling.
- Keep menus and settings consistent with the editor; do not flash bright white surfaces.

## Mode scope

Light mode is the primary scope. A matching dark mode is optional future scope.

## Future implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references for later implementation:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

## Acceptance checklist for later implementation

- [ ] Review the palette for an excessive yellow cast on several displays.
- [ ] Check long notes, tables, properties and code blocks for legibility.
- [ ] Verify that menus and dialogs follow the warm palette.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Original planning scope

The 13 November 2026 task covered repository creation and this design plan.
