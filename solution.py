import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 401164404 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    maximum = x.max()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
#     return loc - scale * norm.ppf(1 - alpha / 2), \
#            loc - scale * norm.ppf(alpha / 2)
    return (maximum - ((maximum-0.017)* norm.ppf(1 - alpha / 2) / np.sqrt(2*len(x))),
           maximum + ((maximum-0.017)* norm.ppf(1 - alpha / 2) / np.sqrt(2*len(x))))
