#!/usr/bin/env python3
"""Basic Sort Algorithms
@author: Raphael Stascheit at MIREVI
"""


def print_colored(arr):
    """Print an array highlighted with the colors available in a terminal.
    This Function builds ANSI-Exception codes from the arrays contents value.
    """
    print("[", end='')
    idx_stop = len(arr) - 1
    for idx, element in enumerate(arr):
        foreground = element % 7 + 30
        background = 48 - element // 7
        ansi_string = '\x1b[0;%s;%sm' % (foreground, background) + str(element) + '\x1b[0m'
        if idx != idx_stop:
            print(ansi_string, end=", ")
        else:
            print(ansi_string, end="]\n")


VERBOSE = True


def bubble_sort(arr):
    arr = arr.copy()
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
                if VERBOSE: print_colored(arr)

    return arr


def selection_sort(arr):
    arr = arr.copy()
    for fillslot in range(len(arr) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if arr[location] > arr[position_of_max]:
                position_of_max = location
            if VERBOSE: print_colored(arr)

        temp = arr[fillslot]
        arr[fillslot] = arr[position_of_max]
        arr[position_of_max] = temp

    return arr


def insertion_sort(arr):
    arr = arr.copy()
    for idx in range(1, len(arr)):
        if VERBOSE: print_colored(arr)
        value = arr[idx]
        pos = idx

        while pos > 0 and arr[pos - 1] > value:
            arr[pos] = arr[pos - 1]
            pos -= 1
            if VERBOSE: print_colored(arr)

        arr[pos] = value

    return arr


if __name__ == '__main__':
    arr_unsorted = [1, 5, 8, 2, 7, 4]

    print("Bubble Sort:")
    print_colored(arr_unsorted)
    bubble_sort(arr_unsorted)

    print("\nSelection Sort:")
    print(arr_unsorted)
    selection_sort(arr_unsorted)

    print("\nInsertion Sort:")
    print(arr_unsorted)
    insertion_sort(arr_unsorted)
