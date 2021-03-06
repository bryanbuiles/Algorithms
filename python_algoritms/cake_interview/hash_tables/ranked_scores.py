"""
    Write a function that takes:
        1) a list of unsorted_scores
        2) the highest_possible_score in the game
    and returns a sorted list of scores in less than O(nlgn) time.
"""
import unittest


def sort_scores(unsorted_scores, highest_possible_score):
    count_score = [0] * (highest_possible_score + 1) # se arma una lista donde los 
                                                    #indices son los valores de la lista sin ordenar y los valores son cuantas veces se repite
    sorted_score = []                                # el elemento
    for score in unsorted_scores:
        count_score[score] += 1 # el numero de veces que esta el score en la lista

    for index in range(len(count_score) - 1, -1, -1):
        contador = count_score[index] # cuantas veces esta repetido el elemento
        for times in range(contador): # loop que hace append dependiendo del numero de veces que esta el elemento

            sorted_score.append(index)
    return sorted_score


class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
