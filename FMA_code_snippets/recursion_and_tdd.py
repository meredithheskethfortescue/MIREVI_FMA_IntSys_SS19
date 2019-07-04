#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def recursive_multiply(a, b, c=0):
    """Returns multiplication of a and b
    :params a: First factor
    :params a: Second factor
    :params c: Sum; Not to be set manually!
    :return: a*b
    """
    if b == 0:
        return c
    elif b > 0:
        return recursive_multiply(a, b - 1, c + a)
    else:
        return recursive_multiply(a, b + 1, c - a)


def recursive_multiply_felix_viering(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return recursive_multiply_felix_viering(a - 1, b) + b


def multiply_florian_lenz(a, b):
    if a == 0:
        return 0
    elif a < 0:
        return -b + multiply_florian_lenz(a + 1, b)
    else:
        return b + multiply_florian_lenz(a - 1, b)


def recursive_divide(a, b, c=0):
    """Returns division of a and b
    :params a: First factor
    :params a: Second factor
    :params c: Quotient; Not to be set manually!
    :return: a/b
    """
    if a == 0:
        return c, 0
    elif a < b:
        return c, a
    else:
        return recursive_divide(a - b, b, c + 1)


def division_philipp_dorn(a, b, c=0):
    if b == 0:
        return None, None
    if a == 0:
        return c, 0
    elif a > 0 and (a - b) >= 0:
        return division_philipp_dorn(a - b, b, c + 1)
    elif a > 0 and (a - b) < 0:
        return c, a


class TestRecursiveImplementation(unittest.TestCase):
    """Test Driven Development approach using the unittest framework"""
    multiplication_implementations_to_test = [
        recursive_multiply,
        recursive_multiply_felix_viering,
        multiply_florian_lenz,
    ]

    division_implementations_to_test = [
        # recursive_divide,
        division_philipp_dorn,
    ]

    def test_multiplication_positive_numbers(self):
        for function in self.multiplication_implementations_to_test:
            self.assertEqual(function(3, 5), 15)

    def test_multiplication_zeros(self):
        for function in self.multiplication_implementations_to_test:
            self.assertEqual(function(0, 5), 0)
            self.assertEqual(function(3, 0), 0)
            self.assertEqual(function(0, 0), 0)

    def test_multiplication_negative_numbers(self):
        for function in self.multiplication_implementations_to_test:
            self.assertEqual(function(-3, 5), -15)
            self.assertEqual(function(3, -5), -15)
            self.assertEqual(function(-3, -5), 15)

    def test_division_no_rest(self):
        for function in self.division_implementations_to_test:
            self.assertEqual(function(9, 3), (3, 0))

    def test_division_with_rest(self):
        for function in self.division_implementations_to_test:
            self.assertEqual(function(9, 2), (4, 1))

    # def test_division_negative(self):
    #     pass

    def test_division_zero(self):
        # todo implement zero test
        for function in self.division_implementations_to_test:
            self.assertEqual(function(5, 0), (None, None))


def test_check_multiplication():
    """Simple testing approach using asserts"""
    functions_to_test = [
        recursive_multiply,
        # recursive_multiply_felix_viering,
        multiply_florian_lenz,
    ]

    for function in functions_to_test:
        assert function(3, 5) == 15
        assert function(0, 5) == 0
        assert function(3, 0) == 0
        assert function(0, 0) == 0
        assert function(-3, 5) == -15
        assert function(3, -5) == -15
        assert function(-3, -5) == 15


if __name__ == '__main__':
    # run simple test implementation
    # test_check_multiplication()
    # print("Simple test implementation passed!")

    # run advanced test implementation using the unittest framework
    unittest.main()
