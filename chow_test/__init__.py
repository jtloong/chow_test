import numpy as np

def f_value(breakpoint, index, y, x):
    def find_rss (y, x):
        A = np.vstack([x, np.ones(len(x))]).T
        rss = np.linalg.lstsq(A, y)[1]
        length = len(y)
        return [rss, length]

    rss_total, n_total = find_rss(y, x)
    rss_1, n_1 = find_rss(np.take(y, np.where(index < breakpoint))[0], np.take(x, np.where(index < breakpoint))[0])
    rss_2, n_2 = find_rss(np.take(y, np.where(index > (breakpoint - 1)))[0], np.take(x, np.where(index > (breakpoint - 1)))[0])

    chow_nom = (rss_total - (rss_1 + rss_2)) / 2
    chow_denom = (rss_1+rss_2) / (n_1 + n_2 - (2 * 2))
    chow = chow_nom / chow_denom
    return chow
