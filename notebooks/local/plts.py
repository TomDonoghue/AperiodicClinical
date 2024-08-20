"""Plotting and helpers for the aperiodic clinical project."""

from pathlib import Path

import matplotlib.pyplot as plt

import seaborn as sns

# Import local utilities
from .utils import sort_df

####################################################################################################
####################################################################################################

COLOR_DEFAULT = '#111dcf'
SHRINK_DEFAULT = 0.8

def plot_hist(df, column, figsize=(3, 2.25), sort=True, end_label=None,
              rotate_x=True, remove_xlabel=True, **kwargs):
    """Helper function to plot a histogram of data."""
    
    # Settings
    color = kwargs.pop('color', COLOR_DEFAULT)
    shrink = kwargs.pop('shrink', SHRINK_DEFAULT)
    
    if sort:
        df = sort_df(df, column, end_label)
    
    plt.figure(figsize=figsize)
    hist = sns.histplot(df, x=column, shrink=shrink, color=color, **kwargs)
    if rotate_x:
        hist.set_xticks(hist.get_xticks())  
        hist.set_xticklabels(hist.get_xticklabels(), rotation=45, ha='right')
    
    if remove_xlabel:
        hist.set(xlabel=None);
        

def savefig(save_fig, file_name, folder=None):
    """Helper function for saving figures."""
    
    save_name = Path('.' if not folder else folder) / file_name
    if save_fig:
        plt.savefig(save_name, bbox_inches='tight')
