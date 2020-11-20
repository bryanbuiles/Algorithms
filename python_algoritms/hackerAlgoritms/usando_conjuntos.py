#!/usr/bin/python3
"""
    retorna el numero de elementos entre las dos arrays que
    son multiplos de la primera array y de la segunda
    ejemplo de uso con conjuntos (set)
"""


def getTotalX(a, b):
    conjunto1 = set()
    conjunto2 = set()
    conjunto4 = set()
    conjunto5 = set()
    for number_1 in a:
        for elemnts in range(a[0], b[0] + 1):
            if elemnts % number_1 == 0:
                conjunto1.add(elemnts)
            else:
                conjunto2.add(elemnts)
    conjunto3 = conjunto1.difference(conjunto2)
    for number_2 in b:
        for elemnts1 in conjunto3:
            if number_2 % elemnts1 == 0:
                conjunto4.add(elemnts1)
            else:
                conjunto5.add(elemnts1)
    print(len(conjunto4.difference(conjunto5)))


getTotalX([2, 4], [16, 32, 96])
