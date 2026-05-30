import numpy as np
import pandas as pd


def psi(expected, actual, buckets=10):
    """
    Population Stability Index (PSI)
    Measures distribution shift between baseline and new data.
    """

    expected = pd.Series(expected).dropna()
    actual = pd.Series(actual).dropna()

    breakpoints = np.percentile(expected, np.linspace(0, 100, buckets + 1))
    breakpoints = np.unique(breakpoints)

    if len(breakpoints) <= 2:
        return 0.0

    expected_counts = np.histogram(expected, bins=breakpoints)[0]
    actual_counts = np.histogram(actual, bins=breakpoints)[0]

    expected_perc = expected_counts / len(expected)
    actual_perc = actual_counts / len(actual)

    expected_perc = np.where(expected_perc == 0, 1e-6, expected_perc)
    actual_perc = np.where(actual_perc == 0, 1e-6, actual_perc)

    psi_value = np.sum(
        (actual_perc - expected_perc) * np.log(actual_perc / expected_perc)
    )

    return float(psi_value)
