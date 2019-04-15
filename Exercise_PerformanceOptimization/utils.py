#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility module
@author: Raphael Stascheit at MIREVI
"""

import math

from matplotlib import pyplot as plt


class PlotCollector:
    def __init__(self):
        """Constructor"""
        self._holding_datasets = []

    def add(self, data):
        """add a new plot"""
        self._holding_datasets.append(data)

    def show(self):
        """Add all holding datasets to the plot and show it"""
        for dataset in self._holding_datasets:
            plt.plot(dataset)

        plt.show()

    def size(self):
        """Get number of holding datasets"""
        return len(self._holding_datasets)


if __name__ == '__main__':
    plot_collector = PlotCollector()
    plot_collector.add([0, 2, 4, 8, 16, 32, 64])
    plot_collector.add([1, 1, 2, 3, 5, 8, 13])
    plot_collector.add([1.] + [math.sin(x) / x for x in range(1, 70)])  # advanced python: list comprehension
    print("Holding", plot_collector.size(), "datasets.")

    plot_collector.show()
