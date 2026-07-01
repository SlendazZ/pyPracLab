import pandas as pd

def concat_frames(frames: list):
    return pd.concat(frames, ignore_index=True)
