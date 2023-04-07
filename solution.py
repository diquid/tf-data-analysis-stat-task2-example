import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1234206085

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    maximum = np.max(x)
    return maximum, (maximum - 0.041) / alpha ** (1/len(x)) + 0.041
