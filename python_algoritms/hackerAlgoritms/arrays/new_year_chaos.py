#!/bin/python3

# New Year Chaos
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# En una fila las personas se pueden intercambiar de posiciones pero solo dos veces
# Cuente el numero de intercambios que se hicieron para la configuracion 'q'

def Organice_file(sorted_list, contador, Dic_contador, Dic_position):
    for index in range(len(sorted_list) - 1, -1, -1):
        if index != 0:
            if Dic_position[sorted_list[index]] <= index and Dic_position[sorted_list[index - 1]] >= index:
                if sorted_list[index] in Dic_contador:
                    if Dic_contador[sorted_list[index]] == 2:
                        contador = "Too chaotic"
                        return contador
                    Dic_contador[sorted_list[index]] += 1
                else:
                    Dic_contador[sorted_list[index]] = 1
                temp = sorted_list[index]
                sorted_list[index] = sorted_list[index - 1]
                sorted_list[index - 1] = temp
                contador += 1
    return contador


def minimumBribes(q):

    sorted_list = sorted(q)
    Dic_position = {}
    Dic_contador = {}
    contador = 0
    for i in range(len(q)):
        Dic_position[q[i]] = i
    while True:
        if sorted_list == q or contador == "Too chaotic":
            print(contador)
            break
        contador = Organice_file(sorted_list, contador,
                                 Dic_contador, Dic_position)


lista = [2, 1, 5, 3, 4]
#lista = [2, 5, 1, 3, 4]
#lista = [1, 2, 5, 3, 4, 7, 8, 6]
#lista = [1, 2, 5, 3, 7, 8, 6, 4]
#lista = [5, 1, 2, 3, 7, 8, 6, 4]

minimumBribes(lista)
