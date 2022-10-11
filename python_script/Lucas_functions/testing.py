import pandas as pd
import numpy as np
from scipy.stats import binom
from scipy.stats import norm
import typing


def standardize(x: pd.Series) -> pd.Series:
    
    x_mean = x.mean()
    x_std = x.std(
    z_score = (x - x_mean)/ x_std
    
    return z_score

path = "/Users/lucaslee/Documents/GitHub/kaggle-data-project/dataset/kaggle_curry/Stephen Curry Stats.csv"


df = pd.read_csv(path)

x = df.FTM.astype(int)
z_score = standardize(x=x)

print(list(x)[:5])
print(z_score.describe())
