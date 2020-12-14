# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
# Organizing Containers of Balls
# Organizar las diferentes bolas en conatiners


def organizingContainers(container):
    dic = {}
    lista = []
    contador = 0
    for rows in range(0, len(container)):
        suma = 0
        for idxcolumns in range(0, len(container[rows])):
            if rows == 0:
                dic[idxcolumns] = container[rows][idxcolumns]
            else:
                dic[idxcolumns] += container[rows][idxcolumns]
            suma += container[rows][idxcolumns]
        lista.append(suma)

    for values in dic.values():
        if values not in lista[contador:]:
            print("Impossible")

    print("Possible")


organizingContainers([[0, 2, 1], [1, 1, 1], [2, 0, 0]])
