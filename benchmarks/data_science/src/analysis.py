import numpy as np
import pandas as pd


def summarize(values: list[int]) -> pd.DataFrame:
    array = np.array(values)
    frame = pd.DataFrame({"value": array})
    return frame.describe()


summary = summarize([1, 2, 3])
