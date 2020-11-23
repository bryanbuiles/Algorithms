"""
    Given a list of integers, find the highest product you can get from three of the integers.
    The input list_of_ints will always have at least three integers.
"""


import unittest


def highest_product_of_3(lista):
    if len(lista) < 3:
        raise ValueError(" minimo 3 elementos")
    mayor = max(lista[0], lista[1])
    menor = min(lista[0], lista[1])
    mayor_producto2 = lista[0] * lista[1]
    menor_producto2 = lista[0] * lista[1]
    mayor_todo = lista[0] * lista[1] * lista[2]
    for numbers in range(2, len(lista)):
        current = lista[numbers]

        mayor_todo = max(mayor_todo, mayor_producto2 *
                         current, menor_producto2 * current)

        mayor_producto2 = max(mayor_producto2, mayor *
                              current, menor * current)

        menor_producto2 = min(menor_producto2, current *
                              mayor, current * menor)

        mayor = max(mayor, current)

        menor = min(menor, current)

    return mayor_todo


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
