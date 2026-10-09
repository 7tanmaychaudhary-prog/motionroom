# Video Editing

A practical agent skill for footage review, editable video assembly, purposeful cutting, captions and motion design, with DaVinci Resolve as the preferred editor.

It combines an editorial workflow with a curated ten-project tool map. It does **not** bundle ten applications, control Resolve on its own, or guarantee a finished professional edit from a single prompt.

## What it helps an agent do

- Review supplied footage and distinguish all-takes assemblies from selective finished edits.
- Preserve project organization, manual changes, full source ranges and audio.
- Choose cuts for story, action, rhythm and continuity; document source ranges and reasons.
- Prepare multilingual captions while preserving approved wording and transliteration.
- Design consistent animated typography, reveals, emphasis and transitions with native titles or official Remotion guidance.
- Plan and attempt tracked behind-subject caption composites using matching foreground footage and correct alpha routing.
- Check results through rendered frames, playback, audio review and actual destination verification.
- Report offline sources, untested timing, failed controls and incomplete work honestly.

## Included toolkit

| Project | Role |
|---|---|
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Media inspection, processing and previews |
| [Official Remotion Skills](https://github.com/remotion-dev/skills) | Motion design and animated captions |
| [AutoSubs](https://github.com/tmoroney/auto-subs) | Subtitle integration |
| [PySceneDetect](https://github.com/Breakthrough/PySceneDetect) | Scene segmentation |
| [Auto-Editor](https://github.com/WyattBlue/auto-editor) | Activity-based draft cuts |
| [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) | Timeline interchange |
| [Whisper](https://github.com/openai/whisper) | Transcription |
| [WhisperX](https://github.com/m-bain/whisperX) | Word alignment and speaker analysis |
| [MoviePy](https://github.com/Zulko/moviepy) | Scripted composition |
| [librosa](https://github.com/librosa/librosa) | Beat and audio analysis |

These are complementary projects selected for adoption and relevance, not a universal ranking. Most are libraries or applications, not agent skills. The skill routes to them when useful; dependencies are installed separately and only when needed. See [toolkit boundaries](references/toolkit.md).

## Install in Codex

Clone this repository into your Codex skills directory as `video-editing`, taking care not to overwrite an existing installation:

```sh
git clone https://github.com/7tanmaychaudhary-prog/video-editing.git ~/.codex/skills/video-editing
```

The entry point is [SKILL.md](SKILL.md). It should be discoverable on your next turn. Other agents supporting Markdown skills may use it, but their integration has not been tested.

Optional official Remotion instructions can be installed separately after reviewing their repository. Installing this skill alone does not install Remotion, FFmpeg, AutoSubs, Python packages, browsers or speech models.

Read-only dependency discovery:

```sh
python3 scripts/check_environment.py
```

This reports availability in the current shell/Python environment; it is not an end-to-end test.

## Example requests

- “Use video-editing to assemble every relevant coffee-preparation take at full length in a vertical timeline.”
- “Review this assembly and propose a 35-second product story before changing it.”
- “Make a snappy cut with varied holds and natural preparation sounds. Preserve my source assembly.”
- “Use consistent white type and yellow emphasis 25% larger, centred inside my guides.”
- “Create a transparent animated title layer; tell me whether it remains editable in Resolve.”

## Motion design

The motion workflow covers hierarchy, typography, easing, frame-based timing, phrase builds, exits and safe bounds. Official Remotion instructions provide the specialist guidance. Native Fusion/Text+ remains preferable when the user needs editable Resolve titles. Remotion renders can be delivered as transparent graphics with editable source retained separately. See [motion design](references/motion-design.md).

## Magic Mask: explicit limitation

The workflow explains foreground duplication, person selection, tracking and alpha routing. In the originating workflow, mask tracking succeeded, but the final alpha connection was blocked by unreliable controls. **A complete autonomous Magic Mask composite is not verified by this package.** It must be tested in the actual Resolve session. Nothing here bypasses that limitation.

## Safety and project preservation

No media uploads, publishing, model downloads or background application changes happen just by loading this skill. The read-only helper only checks dependency discovery. Actual actions follow the user's scope and host permissions. Do not queue mutations into a busy or frozen editor. Avoid automatic DRT exports; use a healthy save/recovery method and preserve user changes.

## Validation status

The skill's structure, links and read-only helper are checked during authoring. The full ten-tool stack is not integration-tested. Existing-source assemblies and caption workflows informed the guidance; they are not a guarantee of tool compatibility on another machine. Treat quality as something demonstrated by the output, not by GitHub stars.

## License and attribution

Original guidance and helper code in this repository are MIT licensed. Linked projects retain their own licenses and terms, including any runtime/commercial terms. Their code is not bundled or relicensed here. Do not include client media, private paths, credentials or conversation transcripts in contributions.
