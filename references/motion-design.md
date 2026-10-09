# Motion design

Use official Remotion skills for code-authored motion: remotion-best-practices for routing, remotion-markup for frame-based animation/layout/typography, remotion-captions for timed language, remotion-render for output and remotion-interactivity for editable controls. These are actual upstream agent skills, not a claim that every toolkit project provides a SKILL.md.

## Design decisions
- Start from the brand, reference and communication purpose. Specify hierarchy, composition, type weight, palette, safe region and motion character before producing the complete sequence.
- Establish a small consistent system: reveal, emphasis, transition and exit. Use position, scale and opacity deliberately; avoid adding every effect simply because available.
- Build timing in frames at the actual composition fps. Use easing for acceleration/deceleration; use spring overshoot only if appropriate to the reference and do not allow it to escape guide boundaries.
- Keep supporting words and emphasized words in consistent size tiers. Account for word lengths, reading time, multiline layout and the full animated bounds.
- Use sound accents and motion beats where they support actions; do not snap every event mechanically to a beat.
- Check beginning, peak and end states, plus full-speed playback. Inspect overlap, ghosting, clipping, flicker, banding and alpha edges. Verify long phrases and mixed-language lines, not only a short attractive sample.

## Resolve handoff
Prefer native Fusion/Text+ when editable Resolve titles are requested and control is reliable. For separate Remotion graphics, retain editable source and timing data, export a verified transparent format appropriate for Resolve, and disclose that imported rendered graphics are not native text layers. Use ProRes 4444 alpha where suitable; follow current official export documentation rather than guessing codec settings. Do not include source footage behind a supposedly transparent title.

## Dependency and licensing check
Skill instructions being installed does not establish the Remotion runtime, browser download, rendering performance or destination compatibility. Check those before promising output. Remotion runtime/commercial terms are separate from this skill repository's license; inspect current official terms for the user's use case. Do not describe a repository's popularity as proof of artistic quality or guarantee a match to a reference before rendering a sample.

Sources: https://github.com/remotion-dev/skills and https://www.remotion.dev/docs/transparent-videos
