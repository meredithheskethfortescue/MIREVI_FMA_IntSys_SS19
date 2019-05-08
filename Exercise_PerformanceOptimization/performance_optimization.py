#!/usr/bin/env python3

"""Sum of multiples of two numbers
If we list all the natural numbers up to 10 that are multiples of 3 or 5
we get 3, 5, 6 and 9. The sum of these multiples is 33.

Find the sum of all the multiples of a or b below n.
When you found your first solution, think again how exactly the described sequence of numbers works.
Try to find a pattern and how you could redesign your algorithm to speed up the calculation time.

Original problem can be found on: https://projecteuler.net/problem=1
@author: Raphael Stascheit
"""

import timeit

import tqdm
import numpy as np


def solution_mod(a, b, n):
    """Straight forward solution
    Declare just one function, that catches every valid value via modulo division.
    """

    sigma = 0  # sum of all multiples

    for it in range(n + 1):  # '+ 1' is necessary because range starts counting at '0'
        if it % a == 0 or it % b == 0:  # check if x is a multiple of a or b; '%' is the modulo operator in python
            sigma += it  # add multiple to the sum

    return sigma


def solution_map(a, b, n):
    """Faster solution by iterating over a map of intervals
    solution_mod is a very easy approach to the problem, but it is inefficient due to the fact that a modulo operation
    is expensive in time. This is obvious if you imagine how a modulo division works inside the machine:
    When calculating 10 mod 3 the computer will subtract 3 from 10 as often as possible and then return the rest.

    The intervals between the multiples will repeat after every multiple of the least common multiple (lcm).
    Thus we can apply the straight forward solution only from 0 to the lcm of a and b and then iterate over the
    intervals between those values.

    Example for a=3, b=5, lcm=15:
    1:            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
    3:            0        3        6        9       12       15       18       21       24       27       30
    5:            0              5             10             15             20             25             30
    map:          0        3     5  6        9 10    12       15       18    20 21       24 25    27       30
    intervals:    |<--3--->|<-2->|-1|<--3--->|-1|<-2->|<--3--->|<--3--->|<-2->|-1|<--3--->|-1|<-2->|<--3--->|
                                                               |
                                                               lcm --> Intervals repeat from here

    Example for a=4, b=6, lcm=12:
    1:            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    4:            0           4           8          12          16          20          24
    6:            0                 6                12                18                24
    map:          0           4     6     8          12          16    18    20          24
    intervals:    |<----4---->|<-2->|<-2->|<----4---->|<----4---->|<-2->|<-2->|<----4---->|
                                                      |
                                                      lcm --> Intervals repeat from here
    """

    # build map of multiples of a and b up to their least common multiple
    # INFO: This has to be done only once, so we can use the modulo function without any concerns.
    map = [0]
    for it in range(1, a * b + 1):
        mod_a = it % a
        mod_b = it % b

        # check for common multiple
        if (0 == mod_a) or (0 == mod_b):
            map.append(it)

        # least common multiple found? (in case that lcm < a*b)
        if (0 == mod_a) and (0 == mod_b):
            break

    # get intervals between the map entries
    intervals = []  # empty list
    for it in range(len(map) - 1):  # intervals is one entry shorter than map
        intervals.append(map[it + 1] - map[it])  # difference of one entry and the next one

    sigma = 0  # sum of all multiples
    multiple = 0  # currently starred multiple of a and b

    # INFO: Here we apply our work a lot of times. Time-expensive functions should be avoided now.
    while multiple <= n:
        for interval in intervals:  # go through map of intervals
            sigma += multiple  # add up new value to the sum
            multiple += interval  # go to the next multiple

            if multiple >= n:  # exit for loop if condition isn't fulfilled anymore
                break

    return sigma


def solution_advanced(a, b, n):
    """This Solution uses advanced programming techniques in python but is slower in this usecase.
    This is only interesting for people who want learn about alternative techniques (generator and list comprehension)
    that can help to write more elegant code in python.
    If you are a beginner in python feel free to skip this!
    """

    # create map of multiples of a and b
    map = [0]
    for multiple in range(1, a * b + 1):
        mod_a = multiple % a
        mod_b = multiple % b

        # check for common multiple
        if (0 == mod_a) or (0 == mod_b):
            map.append(multiple)

        # least common multiple found? (in case that lcm != a*b)
        if (0 == mod_a) and (0 == mod_b):
            break

    # generate intervals via list comprehension
    intervals = [map[i + 1] - map[i] for i in range(len(map) - 1)]

    def generator_loop_array(array):
        """Generator to loops over an array"""
        while True:
            for element in array:
                yield element

    # create a generator which loops over the intervals
    generator_intervals = generator_loop_array(intervals)

    # sum up multiples
    sigma = 0
    multiple = 0
    while multiple <= n:
        sigma += multiple
        multiple += next(generator_intervals)  # get next interval

    return sigma


def solution_sub(a, b, n):
    """Sum up for a and be separately then subtract occuring least common multiples.
        Example for a=3, b=5, lcm=15:
        1:            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
        3:            0        3        6        9       12       15
        5:            0              5             10             15
        common(lcm):  0                                           15
    @author: Marina Kuenzig & Raphael Stascheit
    """

    # find least common multiple
    lcm = None
    for it in range(1, a * b + 1):
        if it % a == 0 and it % b == 0:
            lcm = it
            break

    # sum up a and b to n
    sigma = 0

    for it in range(0, n + 1, a):
        sigma += it

    for it in range(0, n + 1, b):
        sigma += it

    # subtract occuring least common multiples
    for it in range(0, n + 1, lcm):
        sigma -= it

    return sigma


def solution_gauss(a, b, n):
    """Direct calculation of the solution
    Sum up for a and be separately then subtract occurring least common multiples.
    For summing up take advantage of the gaussian sum formula.
        Example for a=3, b=5, lcm=15, n=15:
        1:            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
        3:            0        3        6        9       12       15 occurrences: 5; sum=gaussian_sum(5)*3
        5:            0              5             10             15 occurrences: 3; sum=gaussian_sum(3)*5
        common(lcm):  0                                           15 occurrences: 1; sum=gaussian_sum(1)*15

    Algorithmic efficiency: O(1)
    """

    # find least common multiple
    lcm = None
    for it in range(1, a * b + 1):
        if it % a == 0 and it % b == 0:
            lcm = it
            break

    def gaussian_sum(n):
        """Gaussian sum formula
        returns 1 + 2 + 3 + ... + n
        """
        return (n * (n + 1)) // 2

    # Sum up gaussian sum of occurrences of a and b,
    # then subtract the gaussian sum of the occurences of the least common multiple
    sigma = gaussian_sum(n // a) * a
    sigma += gaussian_sum(n // b) * b
    sigma -= gaussian_sum(n // lcm) * lcm

    return sigma


def auditorium_optimized_loop(a, b, n):
    """Solution from the auditorium:
    Optimized simple loop approach. Uses only two loops. In the second detect collisions with the multiples of the first
    loop. By detecting the bigger one of a and b under certain circumstances some conditions can be skipped.
    @author: Andreas K.
    """
    number_min = min([a, b])
    number_max = max([a, b])

    sigma = 0

    # Sum up multiples of the lower number
    for it in range(0, n + 1, number_min):
        sigma += it

    # Sum up multiples of the bigger number if they are no multiples of the lower number
    for it in range(0, n + 1, number_max):
        if it % number_min != 0:
            sigma += it

    return sigma


def auditorium_set(a, b, n):
    """Solution from the auditorium:
    This approach takes advantage from the set datatype. In a set every value can only exist once.
    Hence the multiples of a and b can added to the set and the detection of multiple occurances can be skipped.
    @author: Created by Rainer; Edited by Raphael Stascheit
    """
    multiples = set()
    n += 1

    for it in range(0, n, a):
        multiples.add(it)

    for it in range(0, n, b):
        multiples.add(it)

    return sum(multiples)


def auditorium_gauss_optimized(a, b, n):
    """Improvement of the gaussian sum by optimizing the calculation of the least common multiple.
    @author: Patrick Nass, edited by Raphael Stascheit
    """
    sigma = 0

    # get least common multiple...
    # todo: explain how
    if a < b:
        lcm = a * b / (b - a)

        if b % a == 0:
            lcm = b
        elif lcm % a != 0:
            lcm = a * b
    else:
        lcm = a * b / (a - b)

        if a % b == 0:
            lcm = a
        elif lcm % b != 0:
            lcm = b * a

    def gaussian_sum(n):
        """Gaussian sum formula
        returns 1 + 2 + 3 + ... + n
        """
        return (n * (n + 1)) // 2

    # Sum up gaussian sum of occurrences of a and b,
    # then subtract the gaussian sum of the occurences of the least common multiple
    sigma = gaussian_sum(n // a) * a
    sigma += gaussian_sum(n // b) * b
    sigma -= gaussian_sum(n // lcm) * lcm

    return sigma


def auditorium_list_comprehension(a, b, n):
    """Oneliner using pythons list comprehension
    Edit: A little boost is possible with a boolean check instead of a comparison with zero. Otherwise it would be a bit
    slower than the naive version.
    @author: Sebastian Rindfleisch, edited by Raphael Stascheit
    """
    return sum(set([x for x in range(1, n + 1) if not x % a or not x % b]))


def solution_numpy(a, b, n):
    """Vectorized version of the naive approach
    This approach disclaims the usage of any for loops. This way we can use vectorized functions from the numpy module.
    """
    arr = np.arange(n + 1)  # array of numbers from 0 to n
    mask = np.logical_or(arr % a == 0, arr % b == 0)  # binary mask of where the condition is True
    return np.sum(arr[mask])  # return sum of them


FLAG_EVALUATE = True
FLAG_VERBOSE = False
STEPS = 9

if __name__ == '__main__':
    # Define parameters
    a, b, n = 3, 5, 10


    def check_function(func):
        """Test if the solution returns the correct results"""
        # Correct result for default values?
        assert func(3, 5, 9) == 23, func.__name__ + "(3, 5, 9) = " + str(func(3, 5, 9)) + " instead of 23"
        # Counting n in or not?
        assert func(3, 5, 10) == 33, func.__name__ + "(3, 5, 10) = " + str(func(3, 5, 10)) + " instead of 33"
        # Concerning about least common multiple or taken a*b by mistake?
        assert func(4, 6, 50) == 408, func.__name__ + "(4, 6, 50) = " + str(func(3, 5, 10)) + " instead of 408"


    solutions = [solution_mod,
                 solution_map,
                 # solution_advanced,
                 solution_sub,
                 solution_gauss,
                 solution_numpy,
                 auditorium_list_comprehension,
                 auditorium_set,
                 auditorium_optimized_loop,
                 auditorium_gauss_optimized]

    # test if solutions are performing correct
    for solution in solutions:
        check_function(solution)
        if FLAG_VERBOSE:
            print(solution.__name__, "passed")

    if FLAG_EVALUATE:
        import time
        import matplotlib.pyplot as plt

        dataset_delta_t = {}

        repetitions = 1  # number of repetitions for time measurement

        # compare different solutions
        for solution in solutions:

            # create empty entry in dictionary
            dataset_delta_t[solution.__name__] = []

            # run solutions for growing parameters
            for step in tqdm.tqdm(range(STEPS), desc=solution.__name__):
                a += step
                b += step
                n = 10 ** step  # exponential growth

                delta_t = timeit.timeit(lambda: solution(a, b, n), number=repetitions) / repetitions
                dataset_delta_t[solution.__name__].append(delta_t)

                # if function needs to much time go to the next one
                if delta_t >= 25.:
                    break

        # bar plot
        plt.figure()  # new figure
        plt.bar(range(len(dataset_delta_t)), [value[-1] for value in dataset_delta_t.values()], align='center')
        plt.xticks(range(len(dataset_delta_t)), list(dataset_delta_t.keys()), rotation=17)

        # line plot
        plt.figure()  # new figure
        print()
        for key, dataset in dataset_delta_t.items():
            # TODO: print sorted dict
            print(key, "\n\t", '{:.8f}'.format(dataset[-1]))
            plt.plot(dataset, label=key, linewidth=4)

        plt.legend(dataset_delta_t)
        plt.show()

    # precise measurement
    repetitions = 1000
    a, b, n = 60, 85, 100000000
    # a, b, n = 3, 5, 100000000
    delta_t_precise_gauss = timeit.timeit(lambda: solution_gauss(a, b, n),
                                          number=repetitions) / repetitions
    delta_t_precise_nass_2 = timeit.timeit(lambda: auditorium_gauss_optimized(a, b, n),
                                           number=repetitions) / repetitions
    print("gauss precise: %f.7" % delta_t_precise_gauss)
    print("nass 2 precise: %f.7" % delta_t_precise_nass_2)
