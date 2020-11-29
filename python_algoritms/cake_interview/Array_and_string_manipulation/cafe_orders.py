#!/usr/bin/python3
"""
    Dadas las tres listas , escriba una función para verificar
    que el servicio de cafe sea por orden de llegada.

    Toda la comida debe salir en el mismo orden en que
    los clientes lo solicitaron (FIFO).
"""

import unittest

# con recursion O(n) O(n)


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


# --------------------------------------cake interview code O(n) O(1)---------------------------------------
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True


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
