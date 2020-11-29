"""
    este algoritmo uso el principio de Pigeonhole en donde n es el numero de espacios disponibles
    y m es el numero de Pigeonhole entonce m > n, el principio nos asegura que al menos dos elementos de m
    estanran juntos en un elemento de n

    este algortimo es util para calcular cuantas evces se repite un numero en O(1) espacio y n(log(n)) tiempo

    Our approach is similar to a binary search, except we divide the range of possible
    answers in half at each step, rather than dividing the list in half.

    1) Find the number of integers in our input list which lie within the range 1..n/2

    2) Compare that to the number of possible unique integers in the same range.

    3)If the number of actual integers is greater than the number
    of possible integers, we know there is a duplicate in the range 1..n/2,
    so we iteratively use the same approach on that range.

    4)If the number of actual integers is not greater than the number of possible integers,
    we know there must be duplicate in the range n/2 + 1..n,
    so we iteratively use the same approach on that range.

    5) At some point, our range will contain just 1 integer, which will be our answer.
"""

import unittest


def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
