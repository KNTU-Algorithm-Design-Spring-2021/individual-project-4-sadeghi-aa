import numpy as np
from numpy import argmin


def assign(num_trucks, weights):
    weights.sort(reverse=True)
    assignments = [[] for _ in range(num_trucks)]
    sum_weight = np.zeros(num_trucks, dtype=int)
    for weight in weights:
        choice = argmin(sum_weight)
        sum_weight[choice] += weight
        assignments[choice].append(weight)
    max_weight = max(sum_weight)
    return assignments, max_weight


if __name__ == '__main__':
    k = 3
    w = [10, 8, 5, 2, 1]

    result, max_w = assign(k, w)
    print('Max Weight with greedy algorithm is', max_w)
    print('Assignments are', result)
