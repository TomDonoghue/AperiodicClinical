"""Plotting and helpers for the aperiodic clinical project."""

from pathlib import Path

import matplotlib.pyplot as plt

import seaborn as sns

from lisc.plts.utils import check_ax, check_aliases

# Import local utilities
from .utils import sort_df

####################################################################################################
####################################################################################################

## SETTINGS
COLOR1 = '#0656a1'    # '#111dcf', '#0b23b0'
COLOR2 = '#a10630'
SHRINK = 0.8


def plot_hist(df, column, figsize=(3, 2.25), sort=True, end_label=None,
              rotate_x=True, remove_xlabel=True, **kwargs):
    """Helper function to plot a histogram of data."""

    # Settings
    color = kwargs.pop('color', COLOR1)
    shrink = kwargs.pop('shrink', SHRINK)

    if sort:
        df = sort_df(df, column, end_label)

    plt.figure(figsize=figsize)
    hist = sns.histplot(df, x=column, shrink=shrink, color=color, **kwargs)
    if rotate_x:
        hist.set_xticks(hist.get_xticks())
        hist.set_xticklabels(hist.get_xticklabels(), rotation=45, ha='right')

    if remove_xlabel:
        hist.set(xlabel=None);


def plot_over_time(data, field, title=None, no_yt=False, ylabel=None, ax=None, **plt_kwargs):
    """Plot data report over time."""

    x_data = list(data.keys())
    y_data = [data[year][field] for year in data.keys()]

    ax = check_ax(ax, plt_kwargs.pop('figsize', (5, 4.5)))

    ax.plot(x_data, y_data,
            linewidth=check_aliases(plt_kwargs, ['linewidth', 'lw'], 4),
            marker=plt_kwargs.pop('marker', '.'),
            markersize=check_aliases(plt_kwargs, ['markersize', 'ms'], 14),
            markerfacecolor=plt_kwargs.pop('markerfacecolor', 'white'),
            color=plt_kwargs.pop('color', COLOR1),
            **plt_kwargs)

    if title:
        ax.set_title(title)

    ax.set_xticks([2020, 2021, 2022, 2023, 2024])
    ax.set_xticklabels(['<2021', '2021', '2022', '2023', '2024'])
    ax.set_xlabel('Year of Publication')

    if no_yt:
        ax.set_yticks([])
    else:
        ax.set_ylabel('Ratio of Papers' if not ylabel else ylabel)

    if max(y_data) < 1.0:
        ax.set_ylim([0, 1.0])


def plot_franges(ranges, ax=None, **plt_kwargs):
    """Plot frequency ranges."""

    ax = check_ax(ax, plt_kwargs.pop('figsize', (4, 8)))
    for ind, crange in enumerate(sorted(ranges)):
        ax.plot(crange, [ind, ind], color=COLOR1)
    ax.set(xlim=[0, 75], ylim=[-1, ind+1], yticks=[], xlabel='Frequency Range');


def savefig(save_fig, file_name, folder=None):
    """Helper function for saving figures."""

    save_name = Path('.' if not folder else folder) / file_name
    if save_fig:
        plt.savefig(save_name, bbox_inches='tight')
