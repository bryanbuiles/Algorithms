"""
    Escriba una funcion eficiente que tome stock prices y
    devuelva el mejor beneficio que podria haber obtenido
    con una compra y una venta de una accion de Apple ayer.

    donde:
        1) Los indices son la hora (en minutos)
        2) Los valores son el precio de una accion en ese momento
"""
import unittest


def get_max_profit(stock_prices):
    if len(stock_prices) == 1:
        raise ValueError("it must be an arrar > 1 element")
    menor = stock_prices[0]
    result = -1000
    for idx_acciones in range(1, len(stock_prices)):
        suma = stock_prices[idx_acciones] - menor
        if stock_prices[idx_acciones] < menor:
            menor = stock_prices[idx_acciones]
        if suma > result:
            result = suma
    return result


class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_primary(self):
        actual = get_max_profit([10, 7, 5, 8, 11, 9])
        expected = 6
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
