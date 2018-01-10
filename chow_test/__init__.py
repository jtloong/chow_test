import numpy as np

# now you can use this function at other points
def find_rss (y, x):
        """
        Return the residual sum of squares and data length.
        # Docstring doesns't mention the types of the input or the expected dimensions
        # example of numpy style docstring:
    
        Parameters
        ----------
        x : ndarray | (N, 1)
            The ...
        
        Output
        ------
        rss : ...
              Resid...
        length : ...
            
        """
        # The code is not robust for x inputs of 1-D or higher
        # By taking the 'len' you assume 0-D array
        # equivalent to 'if x.ndim == 1:'
        if x.ndim == 1:
            # add dimension to x, now col vector
            x = x[:, None]
        A = np.hstack((x, np.ones(x.shape)))
        rss = np.linalg.lstsq(A, y)[1]
        length = len(y)
        # tuples are faster to create than lists
        return (rss, length)


def f_value(breakpoint, index, y, x):
    """Return the f-value of the Chow break test.
    # Docstring doesns't mention the types of the input or the expected dimensions
    example of numpy style docstring:
    
    Parameters
    ----------
    x : ndarray | (N, 1)
        The ...
    
    Output
    ------
    *f-value* : float
                f-value of the Chow break test
    """
    
    rss_total, n_total = find_rss(y, x)
    # Fancy indexing is faster and gives cleaner code
    rss_1, n_1 = find_rss(y[index < breakpoint], x[index < breakpoint])
    rss_2, n_2 = find_rss(y[index > (breakpoint - 1)], x[index > (breakpoint - 1)])

    chow_nom = (rss_total - (rss_1 + rss_2)) / 2
    # 2 * 2 = 4
    # chow_denom = (rss_1 + rss_2) / (n_1 + n_2 - (2 * 2))
    chow_denom = (rss_1 + rss_2) / (n_1 + n_2 - 4)
    # No need to define and than return
    return chow_nom / chow_denom
