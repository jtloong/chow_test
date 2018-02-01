import numpy as np

def f_value(y1, x1, y2, x2):
    """Return the f-value of the Chow break test."""
    def find_rss (y, x):
        """Return the residual sum of squares and data length."""
        A = np.vstack([x, np.ones(len(x))]).T
        rss = np.linalg.lstsq(A, y)[1]
        length = len(y)
        # tuples are faster to create than lists
        return (rss, length)


    rss_total, n_total = find_rss(np.append(y1, y2), np.append(x1, x2))
    rss_1, n_1 = find_rss(y1, x1)
    rss_2, n_2 = find_rss(y2, x2)

    chow_nom = (rss_total - (rss_1 + rss_2)) / 2
    # 2 * 2 = 4
    # chow_denom = (rss_1 + rss_2) / (n_1 + n_2 - (2 * 2))
    chow_denom = (rss_1 + rss_2) / (n_1 + n_2 - 4)
    # No need to define and than return
    return chow_nom / chow_denom
