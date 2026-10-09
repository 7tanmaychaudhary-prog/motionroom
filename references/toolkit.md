# Ten-project toolkit

This is a curated integration map, not a bundled distribution of ten applications or a verified top-ten quality ranking. Check current dependencies, licensing and actual capabilities before use. Install only what the authorized task needs. No third-party code is copied into this public skill.

| Project | Purpose | Boundary |
|---|---|---|
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Probe, extract review material, process and render | Filters/codecs vary by build; not semantic shot selection |
| [Remotion Agent Skills](https://github.com/remotion-dev/skills) | Motion design, captions, typography and rendering guidance | Skill installation is separate from Node/browser/runtime; not Resolve UI control |
| [AutoSubs](https://github.com/tmoroney/auto-subs) | Transcription and subtitle integration | Resolve version/install compatibility requires a small real test |
| [PySceneDetect](https://github.com/Breakthrough/PySceneDetect) | Scene boundaries and review segmentation | Boundaries are candidates, not editorial value judgments |
| [Auto-Editor](https://github.com/WyattBlue/auto-editor) | Activity-based preliminary edits | Do not remove meaningful silence or product-action holds automatically |
| [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) | Structured timeline interchange | Adapters and destination compatibility must be verified; effects may not transfer |
| [Whisper](https://github.com/openai/whisper) | Multilingual transcript draft | Model/runtime resources required; user corrections authoritative |
| [WhisperX](https://github.com/m-bain/whisperX) | Alignment and speaker analysis | Check language-specific alignment support, hardware, models and access conditions |
| [MoviePy](https://github.com/Zulko/moviepy) | Scripted assembly, composition and previews | May flatten edits; use version-appropriate APIs and verify rendering |
| [librosa](https://github.com/librosa/librosa) | Beat, onset and audio-feature analysis | Analysis informs judgment; half/double-tempo ambiguity needs listening |

## Use only the relevant path
- Source inventory: FFprobe and visual/audio review; PySceneDetect when scene segmentation helps.
- Dialogue: one transcription path, with WhisperX only where alignment adds value. AutoSubs when its tested Resolve integration is useful.
- Editing: native Resolve first. Structured cut lists and OTIO for interchange only after destination testing. FFmpeg/MoviePy for previews or requested flattened renders.
- Motion: Remotion skill guidance or native Fusion based on editability requirements.
- Rhythm: librosa when a music grid helps, combined with actual listening and action continuity.

Stars were checked during selection on 2026-10-09 but are intentionally not frozen here as a quality score. Earlier experimental repositories were researched but excluded from this adopted toolkit because their adoption did not meet the user's revised requirement.

## Installation status discipline
Report separately: instructions installed, dependency detected, runtime tested, and real project output verified. Do not equate these states. The public package has no auto-installer for the ten runtimes and does not download models or execute upstream install scripts on invocation.

The authoring session installed the official Remotion instruction bundle at commit `32b241b97f4e0e4ab61fe9a41b05e6e64503f8c5`; recipients should select and inspect an appropriate current revision. It is external, not vendored here.
