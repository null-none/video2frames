import argparse
from video2frames import Video2Frames

# Split input.mp4 into train / val / test datasets
# The input file must be named input.mp4 in the current directory

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
