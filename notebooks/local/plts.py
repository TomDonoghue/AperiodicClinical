"""Plotting and helpers for the aperiodic clinical project."""

from pathlib import Path

import matplotlib.pyplot as plt

import seaborn as sns

from .utils import sort_df

####################################################################################################
####################################################################################################

def plot_hist(df, column, figsize=(3, 3), sort=True, end_label=None, **kwargs):
    """Helper function to plot a histogram of data."""
    
    # Settings
    #color = '#0d72a8'
    color = '#111dcf'
    shrink = 0.8
    
    if sort:
        df = sort_df(df, column, end_label)
    
    plt.figure(figsize=figsize)
    hist = sns.histplot(df, x=column, shrink=shrink, color=color, **kwargs)
    hist.set_xticks(hist.get_xticks())  
    hist.set_xticklabels(hist.get_xticklabels(), rotation=45, ha='right')


def savefig(save_fig, file_name, folder=None):
    """Helper function for saving figures."""
    
    save_name = Path('.' if not folder else folder) / file_name
    if save_fig:
        plt.savefig(save_name, bbox_inches='tight')
