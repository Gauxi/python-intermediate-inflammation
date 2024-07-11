"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


class CSVDataSource():
    def __init__(self, data_path):
        self.data_path = data_path
    def load_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_path}")
        return list(map(models.load_csv, data_file_paths))


def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    inflammation_data = data_source.load_data()
    daily_standard_deviation = compute_standard_deviation_by_day(inflammation_data)

    return daily_standard_deviation

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)


def compute_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation



# def load_inflammation_data(data_path):
#     """
#     Returns a list of 2D NumPy arrays with inflammation data loaded from all 
#     inflammation CSV files found in a specified directory path
#     """
#     data_file_paths = glob.glob(os.path.join(data_path, 'inflammation*.csv'))
#     if len(data_file_paths) == 0:
#         raise ValueError(f"No inflammation data CSV files found in path {data_path}")
#     data = list(map(models.load_csv, data_file_paths))

#     return data

