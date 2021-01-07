#!/bin/python3
"""
    Frequency Queries
    https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
    Cuente la frecuencia de las querry dandole una operacion
    - 1 x : Insert x in your data structure.
    - 2 y: Delete one occurence of y from your data structure, if present.
    - 3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
"""

from collections import defaultdict


def freqQuery(queries):
    lista3 = []
    dicnumber = {}
    dicfrequency = defaultdict(set)
    for querie in queries:
        value = dicnumber.get(querie[1], 0)
        if querie[0] == 1:
            dicnumber[querie[1]] = value + 1
            dicfrequency[value + 1].add(querie[1])
            if value > 0:
                dicfrequency[value].discard(querie[1])
        elif querie[0] == 2:
            if value != 0:
                dicnumber[querie[1]] = value - 1
                if value - 1 > 0:
                    dicfrequency[value - 1].add(querie[1])
                dicfrequency[value].discard(querie[1])
        else:
            lista3.append(1 if dicfrequency[querie[1]] else 0)
    return lista3


q = [[1, 1], [2, 2], [3, 2], [1, 1], [1, 1], [2, 1], [3, 2]]
q = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 5], [3, 2]]
q = [[1, 64], [1, 16777216], [3, 17], [2, 32768], [
    1, 1], [2, 32], [3, 22], [2, 2097152], [3, 34]]
print(freqQuery(q))
