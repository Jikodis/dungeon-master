# TODO

Upcoming features, known gaps, and ideas worth considering. Not a sprint plan — a parking lot. Move items into `docs/superpowers/specs/` when promoting them to actual work.

## Skills worth adding later

- **`prep/level-up`.** When a PC hits a new level, walk through the changes (HP increase, new features/spells, ASI/feat decisions). Currently has to be improvised.
- **`prep/downtime`.** Between-adventure crafting, training, carousing, lifestyle expenses. Not addressed in the spec; becomes important around level 5+.
- **`prep/handouts` (player-facing handouts).** No skill yet generates handouts (letters, posters, journal entries the players see). Could live under `prep/handouts/`.
- **`prep/magic-item`.** Generate a custom magic item that fits the campaign's tone (currently low-magic). Partially overlaps with `prep/encounters` treasure work — split if it grows.
- **`live/turn-prompt`.** "Whose turn is it, what are their reactions/conditions, what enemies are still up?" — initiative tracking is explicitly out of scope for the OS, but a thin live skill that summarizes the active turn from a DM-supplied state would help. Other tools already do this well; only build if the friction shows up in real play.

## Bigger ideas

- **Map parsing.** Skills currently treat maps as opaque references. If desired, a future skill could call vision tools to describe a battle map.
- **Player-facing handouts.** No skill yet generates handouts (letters, posters, journal entries the players see). Could be added under `prep/handouts`.
- **Campaign analytics.** Once 50+ sessions exist, a `campaign-analytics` skill could surface "PCs we've under-served," "threads stale > 5 sessions," etc. Out of POC scope.
- **OneNote migration tooling.** User will do the export manually; no helper skill yet. If migration is painful, a `migrate-onenote-page` skill could parse exported HTML.

## Rules / SRD upgrades

- **Move to 2024 rules SRD (5.2.1) when the table converts.** The vendored SRD is 5.1 (2014 rules + Nov 2018 errata) per [oldmanumby/dnd.srd](https://github.com/OldManUmby/dnd.srd). When the campaign upgrades to the 2024 PHB rules, swap `context/rules/srd/` for a 5.2.1 Markdown source and update `context/rules/srd/_INDEX.md`. Skills only depend on the path — no code changes needed.
- **Magic items.** SRD covers a subset; full DMG items aren't there. If `prep/magic-item` is built, decide whether to ground it in SRD items only (safe) or allow model-knowledge fallback labeled `(unverified — not in SRD)`.

## Conventions / spec drift to clean up

- **`PCs/` `arc_state` typing.** Currently mixes kebab-case slugs and freeform parentheticals (e.g. `searching-for-brother (currently dormant lead)`). Pick one convention; if anything ever filters by `arc_state`, the parenthetical breaks comparisons. Possibly add `arc_notes:` for prose.
- **`parent_location: none`.** Unidiomatic YAML (`none` parses as the string `"none"`). Either omit when empty or use `null`.
- **`<!-- last updated: prep -->` ambiguity.** The marker can't distinguish "between session 18 and 19" from "between session 22 and 23". Consider `prep-pre-sNN` or include a date.
- **Stub NPC files for "mentioned but not statted" recurring names** (e.g. Factor Renn). Decide whether `live/who-knows-what` should fail open or fall back to "no file — likely a minor NPC."
- **Session frontmatter schema** for `prep` sessions vs completed sessions isn't documented in the spec — only the completed-session schema is shown. Codify.

## Documentation

- **Spec/plan are historical artifacts** in `docs/superpowers/specs/` and `docs/superpowers/plans/`. They reference the original `skills/` path layout, not the current `.agents/skills/`. Either update them or add a "this is a snapshot of the original design — see CLAUDE.md and tour for current state" preamble.

## Operational

- **Branch protection on `main`** is enabled (direct agent pushes are blocked). All future agent commits land in feature branches.
- **CI / linters.** None today. Worth considering: a YAML-frontmatter validator for entity files, an `_INDEX.md` consistency checker, and a SKILL.md frontmatter validator. All would be Markdown linters, not gameplay code.
