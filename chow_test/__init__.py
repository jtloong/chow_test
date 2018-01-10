import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def f_value(break_point, data, timeColumn, x_column, y_column):
    def find_rss (data, x_column, y_column):
        x = data[[x_column]]
        y = data[y_column]
        lm = LinearRegression()
        lm.fit(x, y)
        rss = np.sum(np.square(y - lm.predict(x)))
        return rss
    data = data.dropna()
    rss_total = find_rss(data, x_column, y_column)
    rss_1 = find_rss(data[data[timeColumn] < break_point], x_column, y_column)
    rss_2 = find_rss(data[data[timeColumn] > (break_point - 1)], x_column, y_column)
    n_1 = len(data[data[timeColumn] < break_point])
    n_2 = len(data[data[timeColumn] > (break_point - 1)])
    chow_nom = (rss_total - (rss_1 + rss_2)) / 2
    chow_denom = (rss_1+rss_2) / (n_1 + n_2 - (2 *2))
    chow = chow_nom / chow_denom
    return chow
