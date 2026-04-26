---
name: locations
description: Use when DESIGNING a new location (tavern, dungeon, town, wilderness area) or expanding an existing one with sub-locations or detail. Reads campaign tone and parent region for consistency. Writes to context/locations/<type>/<slug>.md after proposing changes.
---

# Locations (prep skill)

## When to use
- "Create a tavern in <town>" → file in `context/locations/towns/`.
- "Design a dungeon for <quest>" → file in `context/locations/dungeons/`.
- "Expand <existing location> with more detail" → modifies the existing file.
- "Add a sub-location to <town>" → new file with `parent_location` set.

## When NOT to use
- At the table when you need a place to drop the party that doesn't matter long-term. Use `live/improvise-location`.
- For maps as images. Maps go in `context/maps/`; this skill only handles the textual location notes.

## Inputs
- `context/campaign.md` — tone.
- `context/world/geography.md` — regional context.
- The parent location file if one exists.
- Related quest files if the location ties to a quest.

## Workflow

### New location
1. Read campaign tone + region.
2. Read parent location (if any) and any tied quest.
3. Draft frontmatter + sections.
4. **Propose** the file path, frontmatter, and section outline. Wait for approval.
5. On approval: write the file with the `<!-- last updated: sNN -->` footer (use `prep` if between sessions). Update `context/locations/_INDEX.md`.

### Expanding an existing location
1. Read existing file.
2. Identify what's being added (sub-locations, encounter hooks, history).
3. Propose the diff. Wait for approval.
4. On approval: write changes; update the footer.

## Output conventions

Location files have these sections (vary slightly by type):
1. Frontmatter (name, type, region, parent_location, tags; type-specific: population, governance, tier)
2. `## Overview` — 2-3 sentences setting the place
3. `## Districts` (towns) / `## Layout` (dungeons) / `## Terrain` (wilderness)
4. `## Notable locations` (towns/dungeons) — list of sub-points
5. `## Mood` (towns) — sensory; what does it feel like
6. `## Inhabitants` / `## Who's there` — who's around
7. `## Hooks` or `## Encounters` — uses for play
8. Footer.

For dungeons specifically:
- Always include hazards section.
- Always include "DM-known" content marked separately from player-discoverable.

## Update rules
- Always update `context/locations/_INDEX.md` when writing a file.
- Always update the footer.
- When a location's status changes (e.g., destroyed, captured by faction X), preserve previous status in a History section.
