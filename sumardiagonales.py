""" sumar las diagonales y luego calcular la diferencia """


def diagonalDifference(arr):
    contador1 = 0
    sumrigth = 0
    contador2 = len(arr[0]) - 1
    sumleft = 0
    for array in arr:
        for index in range(len(array) + 1):
            if contador1 == index:
                sumrigth += array[index]
        contador1 += 1

        for index in range(len(array) - 1, - 1, -1):
            if contador2 == index:
                sumleft += array[index]
        contador2 -= 1
    return(abs(sumleft - sumrigth))


print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
