# coding: utf-8
import numpy as np

__author__ = "Adrien Guille"
__email__ = "adrien.guille@univ-lyon2.fr"


def erdem_correlation(array_1, array_2):
    a_12 = 0.
    a_1 = 0.
    a_2 = 0.
    for i in range(1, len(array_1)):
        a_12 += (array_1[i] - array_1[i-1]) * (array_2[i] - array_2[i-1])
        a_1 += (array_1[i] - array_1[i-1]) * (array_1[i] - array_1[i-1])
        a_2 += (array_2[i] - array_2[i-1]) * (array_2[i] - array_2[i-1])
    a_1 = np.sqrt(a_1/(len(array_1) - 1))
    a_2 = np.sqrt(a_2/(len(array_2) - 1))
    coefficient = a_12/(len(array_1) * a_1 * a_2)
    return coefficient


def overlap_coefficient(interval_0, interval_1):
    intersection_cardinality = float(min(interval_0[1], interval_1[1]) - max(interval_0[0], interval_1[0]))
    smallest_interval_cardinality = float(min(interval_0[1] - interval_0[0], interval_1[1] - interval_1[0]))
    
    if(smallest_interval_cardinality==0):
        return 0
    
    return float(intersection_cardinality / smallest_interval_cardinality)
