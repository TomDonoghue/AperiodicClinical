# Aperiodic Clinical Review

`AperiodicClinical` project repository: a systematic review of clinically related studies of aperiodic activity.

## Overview

The study of aperiodic neural activity has rapidly become a common feature of interest in clinical investigations. This rapid proliferation of studies of aperiodic activity across a wide range of disorders has led to a rapidly emerging literature in which multiple different lines across different disorders are seeking to evaluate if and how aperiodic neural activity may be relevant and useful in clinical neuroscience, including as a putative biomarker. This review project seeks to evaluate the current status of clinically-related work with aperiodic activity, across all disorders, to evaluate the set of shared findings and challenges, and use this information to present suggestions for future work investigation aperiodic activity in the context of clinical disorders.

## Project Guide

You can step through all the analyses and results in this project by stepping through the `notebooks`.

## Reference

Preprint for this project upcoming.

## Requirements

This project was written in Python 3 and requires Python >= 3.8 to run.

If you want to re-run this project, you will need some external dependencies.

- [specparam](https://github.com/fooof-tools/fooof) >= 2.0.0
- [neurodsp](https://github.com/neurodsp-tools/neurodsp) >= 2.3.0
- [lisc](https://github.com/lisc-tools/lisc) >= 0.4.0

You can install the extra required dependencies by running:

```
pip install specparam, neurodsp, lisc
```

## Repository Layout

This project repository is set up in the following way:

- `data/` includes data from the project, including the literature data
- `notebooks/` includes Jupyter notebooks that step through the project and create the figures
- `prisma/` includes filled out PRISMA checklists for this project as a systematic review

## Data

This project uses some simulated data as examples, and mainly examines literature data.

The simulations are done with the [neurodsp](https://github.com/neurodsp-tools/neurodsp) and [specparam](https://github.com/fooof-tools/fooof) modules for time domain and frequency domain simulations respectively.

The literature data is from a systematic review and structured analysis of a the collected literature.
