"""Utilities for the aperiodic-clinical project."""

from collections import Counter

import numpy as np
import pandas as pd

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

def sort_df(df, column, end_label=None, copy=True):
    """Sort the entries in a dataframe by count."""
    
    if copy:
        df = df.copy()    
    
    labels = [el[0] for el in Counter(df[column]).most_common()]
    
    if end_label:
        for el in [end_label] if isinstance(end_label, str) else end_label:
            labels.remove(el)
            labels = labels + [el]

    df[column] = pd.Categorical(df[column], labels)
    
    return df


def min_count(df, column, min_value):
    """Helper function for sub-selecting a minimum number of values."""
    
    return df.groupby(column).filter(lambda x : len(x) > min_value)


def replace_multi_str(df, column, fill='multiple'):
    """Replace entries with multiple values with a string."""
    
    split = '\u2028'
    multicol = df[column].str.contains(split).values
    for rind, row in df[multicol].iterrows():
        df.loc[rind, column] = fill
    
    return df


def replace_multi_int(df, column):
    """Replace entries with multiple values with the sume."""
    
    split = '\u2028'
    dubvals = df[column].str.contains(split).values
    for rind, row in df[dubvals].iterrows():
        df.loc[rind, column] = sum([int(el) for el in row[column].split(split)])
        
    return df


def replace_other(df, column, min_val):
    """Replace infrequent items with an 'other' category."""

    df = df.copy()
    
    counts = Counter(df[column])
    
    kept = [label for label, count in counts.items() if count >= min_val]
    dropped = [label for label, count in counts.items() if count < min_val]
    
    df = df.replace(dropped, 'other')
    df[column] = pd.Categorical(df[column], kept + ['other'])    
    
    return df
