"""
    You have a list of integers, and for
    each index you want to find the product of every
    integer except the integer at that index.
"""
import unittest


def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise ValueError("debe ser + de un elemento")
    n = 1
    multiplication = 1
    multiplicacion_antes = [None] * len(int_list)
    multiplicacion_result = [None] * len(int_list)

    # estamos recorriendo la lista de atras hacia delante y acomulando
    # el producto de cada integer, excepto en ese indice ejemplo [540, 270, 45, 9, 1]
    for integer_adentro in range(len(int_list) - 1, -1, -1):
        multiplicacion_result[integer_adentro] = multiplication
        multiplication *= int_list[integer_adentro]

    # estamos recorreindo la lista desde el principio y acomulando
    # el producto de cada integer excepto en ese indice ejemplo [1, 1, 2, 12, 60]
    for integer in range(len(int_list)):
        multiplicacion_antes[integer] = n
        n *= int_list[integer]
        # recordar Multiplicacion_result es la lista con los valores acomulados antes
        # del indice
        multiplicacion_result[integer] = multiplicacion_antes[integer] * \
            multiplicacion_result[integer]

    return multiplicacion_result


class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)
