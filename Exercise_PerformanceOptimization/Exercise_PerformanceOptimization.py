#!/usr/bin/env python3

"""Sum of multiples of two numbers
If we list all the natural numbers below 10 that are multiples of 3 or 5
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of a or b below n.
When you found your first solution, think again how exactly the described sequence of numbers works.
Try to find a pattern and how you could design an algorithm to speed up the calculation time.

Original problem can be found on: https://projecteuler.net/problem=1
@author: Raphael Stascheit
"""

import timeit


def solution_mod(a, b, n):
    """Straight forward solution
    Declare just one function, that catches every valid value via modulo division.
    """

    sigma = 0  # sum of all multiples

    for x in range(n + 1):  # '+ 1' is necessary because range starts counting at '0'
        if x % a == 0 or x % b == 0:  # check if x is a multiple of a or b; '%' is the modulo operator in python
            sigma += x  # add multiple to the sum

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
    """Sum up for a and be separately then subtract occurring least common multiples.
    For summing up take advantage of the gaussian sum formula.
        Example for a=3, b=5, lcm=15, n=15:
        1:            0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
        3:            0        3        6        9       12       15 occurrences: 5; sum=gaussian_sum(5)*3
        5:            0              5             10             15 occurrences: 3; sum=gaussian_sum(3)*5
        common(lcm):  0                                           15 occurrences: 1; sum=gaussian_sum(1)*15
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


def clueless(a, b, n):
    summe = 0

    for i in range(0, n, a):
        summe += i

    for i in range(0, n, b):
        if i % a != 0:
            summe += i

    return summe


def solution_very_simple(a, b, limit=10):
    # Rainer
    my_list = []
    _a = a
    _b = b

    while a < limit:
        my_list.append(a)
        a += _a

    while b < limit:
        my_list.append(b)
        b += _b

    return sum(set(my_list))


EVALUATE = True

if __name__ == '__main__':
    # Define parameters
    # a, b, n = 3, 5, 10
    a, b, n = 150, 640, 1000000

    print(solution_mod(a, b, n))
    print(solution_map(a, b, n))
    print(solution_advanced(a, b, n))
    print(solution_sub(a, b, n))
    print(solution_gauss(a, b, n))
    print(clueless(a, b, n))
    print()

    if EVALUATE:
        repetitions = 50

        time_mod = timeit.timeit(lambda: solution_mod(a, b, n), number=repetitions) / repetitions
        print("modulo naive  ", time_mod)

        time_map = timeit.timeit(lambda: solution_map(a, b, n), number=repetitions) / repetitions
        print("map           ", time_map)

        time_adv = timeit.timeit(lambda: solution_advanced(a, b, n), number=repetitions) / repetitions
        print("advanced      ", time_adv)

        time_sub = timeit.timeit(lambda: solution_sub(a, b, n), number=repetitions) / repetitions
        print("subtract      ", time_sub)

        time_gauss = timeit.timeit(lambda: solution_gauss(a, b, n), number=repetitions) / repetitions
        print("gauss         ", time_gauss)

        time_clueless = timeit.timeit(lambda: clueless(a, b, n), number=repetitions) / repetitions
        print("clueless      ", time_clueless)

        time_solution_very_simple = timeit.timeit(lambda: solution_very_simple(a, b, n),
                                                  number=repetitions) / repetitions
        print("solution_very_simple      ", time_solution_very_simple)

        print()
        print("map is %.3f times faster." % (time_mod / time_map))
        print("gauss is %.3f times faster." % (time_mod / time_gauss))
