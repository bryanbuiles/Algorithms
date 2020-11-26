"""
    Encontrar el punto de rotacion de una lista de palabaras ordenadas

    tengo una lista de palabras que son en su mayoria alfabeticas,
    excepto que comienzan en algun lugar en el medio del alfabeto, llegan al final y
    luego comienzan desde el principio del alfabeto. En otras palabras,
    se trata de una lista ordenada alfabeticamente que se ha rotado.
"""

import unittest

# use binary search para encontrar la palabra


def find_rotation_point(words):

    floor_index = -1  # floor es el indice menor de piso
    ceiling_index = len(words)  # celling es el indixe mayor
    final_word = words[-1]
    if ceiling_index < 2 or words[0] < final_word:
        return 0

    # aplicando binary search
    while floor_index + 1 < ceiling_index:
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        rotation_index = floor_index + half_distance
        rotation_value = words[rotation_index]

        # si la palabrar anteior es mayor es el punto de rotacion
        if words[rotation_index - 1] > rotation_value:
            return rotation_index
        # a la derecha de la mitad
        if rotation_value >= final_word:
            floor_index = rotation_index
        # a la izquierda de la mitad
        else:
            ceiling_index = rotation_index
    return -1


class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    def test_letters_list(self):
        actual = find_rotation_point(
            ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i'])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
