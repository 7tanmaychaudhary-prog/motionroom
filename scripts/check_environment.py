#!/usr/bin/env python3
"""Read-only dependency discovery. Does not import packages, install or launch apps."""
import importlib.util
import json
import shutil

def main():
    report = {'commands': {}, 'python_modules': {}, 'limits': 'Discovery only. No rendering, Resolve connection, model availability or compatibility test performed.'}
    for name in ['ffmpeg', 'ffprobe', 'node', 'npm', 'auto-editor', 'scenedetect', 'whisper']:
        report['commands'][name] = bool(shutil.which(name))
    for name in ['opentimelineio', 'whisper', 'whisperx', 'moviepy', 'librosa', 'scenedetect']:
        try:
            report['python_modules'][name] = importlib.util.find_spec(name) is not None
        except (ImportError, ValueError):
            report['python_modules'][name] = False
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
