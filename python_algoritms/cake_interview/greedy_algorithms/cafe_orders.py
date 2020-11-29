#!/usr/bin/python3
"""
    Dadas las tres listas , escriba una función para verificar
    que el servicio de cafe sea por orden de llegada.

    Toda la comida debe salir en el mismo orden en que
    los clientes lo solicitaron (FIFO).
"""

import unittest

# take_out_index = index de las ordenes de salida
def cafe_order(served_orders, take_out_orders, dine_in_orders,
               served_index=0, take_out_index=0, diner_index=0):

    if take_out_index < len(take_out_orders) and \
            take_out_orders[take_out_index] == served_orders[served_index]:
        take_out_index += 1
    elif diner_index < len(dine_in_orders) and \
            dine_in_orders[diner_index] == served_orders[served_index]:
        diner_index += 1
    else:
        return False
    served_index += 1
    if served_index >= len(served_orders):
        return True

    return cafe_order(served_orders, take_out_orders, dine_in_orders,
                      served_index, take_out_index, diner_index)


class TestCafe_order(unittest.TestCase):

    def test_case1(self):
        current = cafe_order([17, 8, 12, 19, 24, 2], [17, 8, 24], [12, 19, 2])
        expect = True
        self.assertEqual(current, expect)

    def test_case2(self):
        current = cafe_order([1, 2, 4, 6, 5, 3], [1, 3, 5], [2, 4, 6])
        expect = False
        self.assertEqual(current, expect)

    def test_case3(self):
        current = cafe_order([17, 8, 12, 19, 24, 2, 5, 6], [
                             17, 8, 24, 5, 6], [12, 19, 2])
        expect = True
        self.assertEqual(current, expect)

    def test_case4(self):
        current = cafe_order([17, 8, 12, 19, 24, 2, 5], [
                             17, 8, 24, 5], [12, 19, 2])
        expect = True
        self.assertEqual(current, expect)

    def test_case5(self):
        current = cafe_order([17, 8, 12, 2, 24, 19], [17, 8, 24], [12, 19, 2])
        expect = False
        self.assertEqual(current, expect)


if __name__ == '__main__':
    unittest.main()
