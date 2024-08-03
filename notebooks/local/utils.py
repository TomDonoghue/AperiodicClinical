"""Utilities for the aperiodic-clinical project."""

import numpy as np

from specparam.utils import trim_spectrum

####################################################################################################
####################################################################################################

## TIME SERIES ANALYSIS UTILS

AVG_FUNCS = {
    'mean' : np.mean,
    'median' : np.median,
    'sum' : np.sum
}

def compute_abs_power(freqs, powers, band, method='sum'):
    """Compute absolute power for a given frequency band."""

    _, band_powers = trim_spectrum(freqs, powers, band)
    avg_power = AVG_FUNCS[method](band_powers)

    return avg_power

## DATAFRAME MANAGEMENT UTILS

def min_count(df, column, min_value):
    """Helper function for sub-selecting a minimum number of values."""
    
    return df.groupby(column).filter(lambda x : len(x) > min_value)
