"""Instructor-supplied input preparation. Students change the arguments only."""
from pathlib import Path
import warnings
import numpy as np
from scipy import signal as sp

DATA = Path(__file__).resolve().parent / 'data'


def get_co2(start_year=2010, years=10, product='monthly', detrend=False):
    """Return elapsed time [years], concentration/departure [ppm], samples/year.

    Monthly observations use a regular month index, not equal-length months in
    days. Annual means are the actual NOAA annual product. By default the
    published concentrations are returned unchanged. A true detrend flag
    subtracts a straight line within the selected interval. Original files
    remain unchanged. Whole years only, with the end year excluded.
    """
    if int(years) != years or years < 1:
        raise ValueError('Choose a positive whole number of years.')
    if product == 'monthly':
        table = np.loadtxt(DATA / 'co2_mm_mlo.txt', comments='#')
        selected = table[(table[:, 0] >= start_year) & (table[:, 0] < start_year + years)]
        samples = selected[:, 3].copy()  # Published concentration, not seasonally adjusted column.
        sampling_rate = 12
        month_index = 12 * selected[:, 0] + selected[:, 1]
        if not np.all(np.diff(month_index) == 1):
            raise ValueError('The selected month indices are not consecutive.')
        if np.any(selected[:, 6:8] < 0):
            warnings.warn('Some selected months have unavailable variability metadata or interpolation flags. Inspect the source rows.')
    elif product == 'annual':
        table = np.loadtxt(DATA / 'co2_annmean_mlo.txt', comments='#')
        selected = table[(table[:, 0] >= start_year) & (table[:, 0] < start_year + years)]
        samples = selected[:, 1].copy()
        sampling_rate = 1
        if not np.all(np.diff(selected[:, 0]) == 1):
            raise ValueError('The selected years are not consecutive.')
    else:
        raise ValueError("Choose product='monthly' or product='annual'.")
    if len(samples) != years * sampling_rate or not np.all(samples > 0):
        raise ValueError('Choose complete years with available concentration measurements.')
    if detrend:
        samples = sp.detrend(samples, type='linear')
    time = np.arange(len(samples)) / sampling_rate
    return time, samples, sampling_rate
