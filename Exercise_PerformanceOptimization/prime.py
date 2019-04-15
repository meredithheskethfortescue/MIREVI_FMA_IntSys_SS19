#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple approach to find prime numbers
@author: Raphael Stascheit at MIREVI
"""


def is_prime(number):
    for it in range(2, number):
        if 0 == number % it:
            return False

    return True


primes = []

for it in range(2, 1000 + 1):
    if is_prime(it):
        primes.append(it)

print(primes[11])
print(primes)
