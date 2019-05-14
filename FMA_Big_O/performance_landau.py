import time
import timeit
import math

import tqdm
import matplotlib.pyplot as plt


def gaussian_sum_1(n):
    """Gaussian sum formula
    returns 1 + 2 + 3 + ... + n
    Aufwand: O(1)
    """
    return (n * (n + 1)) // 2


def gaussian_sum_n(n):
    """Aufwand: O(n)"""
    sigma = 0
    for it in range(n):
        sigma += n

    return sigma


def example_square(n):
    """O(n²)"""
    for row in range(n):
        for column in range(n):
            do_stuff()


def example_log(n):
    """O(log(n))"""
    i = 1
    while i < n:
        do_stuff()
        i = i * 2


def function_a(n):
    t = 3 * n * (n - 1) * (n + 1) - 3 * n
    time.sleep(t / 100000)


def function_b(n):
    t = 10 * n - n * math.log(n) + 15
    time.sleep(t / 100000)


def c1(n):
    for __ in range(n):
        function_a(n)
        function_b(n)


def c2(n):
    i = 1
    while i < n:
        if 4 < 5:
            function_b(n)
        function_a(n)
        i = i * 2


def c3(n):
    for i in range(n):
        function_a(n)
        for j in range(n):
            function_b(n)


if __name__ == '__main__':
    steps = 20
    stepwidth = 1
    repetitions = 1  # number of repetitions for time measurement

    functions = [c1, c2, c3]

    dataset_delta_t = {}

    # compare different solutions
    for solution in functions:

        # create empty entry in dictionary
        dataset_delta_t[solution.__name__] = []

        # run solutions for growing parameters
        for step in tqdm.tqdm(range(3, steps * stepwidth, stepwidth), desc=solution.__name__):
            delta_t = timeit.timeit(lambda: solution(step), number=repetitions) / repetitions
            dataset_delta_t[solution.__name__].append(delta_t)

            # if function needs to much time go to the next one
            if delta_t >= 25.:
                break

    # line plot
    print()
    for key, dataset in dataset_delta_t.items():
        plt.plot(dataset, label=key, linewidth=4)

    plt.legend(dataset_delta_t)
    plt.show()
