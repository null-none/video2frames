# Video2Frames

Simple python script to convert a video file to frames as jpg files.

---

## Using the `Video2Frames` class

The `Video2Frames` class can be used directly from Python without the command line.

```python
import argparse
from video2frames import Video2Frames

args = argparse.Namespace(
    input="input.mp4",
    output="dataset/train",
    maxframes=None,
    rotate=None,
    exifmodel=None,
    verbose=False,
)

v2f = Video2Frames()
ret = v2f.start(args)
print("Exit code:", ret)
```

---

## Examples with train / val / test splits

A common use case: split a single `input.mp4` into three dataset splits.

```python
import argparse
from video2frames import Video2Frames

v2f = Video2Frames()

# (output_folder, max_frames)
splits = [
    ("dataset/train", 500),
    ("dataset/val",   100),
    ("dataset/test",  100),
]

for output_dir, maxframes in splits:
    args = argparse.Namespace(
        input="input.mp4",
        output=output_dir,
        maxframes=maxframes,
        rotate=None,
        exifmodel=None,
        verbose=True,
    )
    ret = v2f.start(args)
    print(f"{output_dir} -> exit code {ret}")
```

Output folder structure:

```
dataset/
├── train/   # 500 frames evenly sampled across the video
│   ├── frame_0.jpg
│   ├── frame_1.jpg
│   └── ...
├── val/     # 100 frames
│   └── ...
└── test/    # 100 frames
    └── ...
```

> The input file is always named `input.mp4` and must be in the current working directory (or provide a full path).

---

## Command line

```
python video2frames.py input.mp4 <output_folder> [--maxframes=N] [--rotate={90,180,270}] [--exifmodel=<photo>] [--verbose]
```

### Options

| Option | Description |
|---|---|
| `--maxframes=N` | Maximum number of output frames |
| `--rotate={90,180,270}` | Rotate frames clock-wise |
| `--exifmodel=<photo>` | Example photo to copy EXIF tags from |
| `--verbose` | Enable verbose output |

### Examples

1. Split video into frames:
```
python video2frames.py input.mp4 dataset/train
```

2. All three splits (shell):
```bash
python3 video2frames.py input.mp4 dataset/train --maxframes=550
python3 video2frames.py input.mp4 dataset/val   --maxframes=120
python3 video2frames.py input.mp4 dataset/test  --maxframes=120
```
