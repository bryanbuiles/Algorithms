"""
Su empresa creó una herramienta de calendario interna llamada HiCal.
Desea agregar una función para ver las horas en un día en que todos están disponibles.

Para hacer esto, necesitará saber cuándo un equipo tiene una reunión.
En HiCal, una reunión se almacena como una tupla de enteros (start_time, end_time).
Estos números enteros representan el número de bloques de 30 minutos después de las 9:00 am.

Algoritmo: O(n^2)
"""


def merge_ranges(arr):
    lista = []
    lista2 = []
    flag = 0
    for index in range(len(arr)):
        if arr[index] in lista2:
            continue
        for elements in arr[index:]:
            if arr[index][1] == elements[0] and arr[index] is not elements:
                if arr[index] not in lista:
                    if arr[index][0] < elements[0]:
                        lista.append((arr[index][0], elements[1]))
                        lista2.append(elements)
                    else:
                        lista.append((elements[0], elements[1]))
                        lista2.append(elements)
                flag = 1
            elif arr[index][1] > elements[1] and arr[index] is not elements and arr[index][1] >= elements[0]:
                if arr[index] not in lista:
                    if arr[index][0] < elements[0]:
                        lista.append((arr[index][0], arr[index][1]))
                        lista2.append(elements)
                    else:
                        lista.append((elements[0], arr[index][1]))
                        lista2.append(elements)
                flag = 1
            elif arr[index][1] < elements[1] and arr[index] is not elements and arr[index][1] >= elements[0]:
                if arr[index] not in lista:
                    if arr[index][0] < elements[0]:
                        lista.append((arr[index][0], elements[1]))
                        lista2.append(elements)
                    else:
                        lista.append((elements[0], elements[1]))
                        lista2.append(elements)
                flag = 1
        if flag == 0:
            lista.append((arr[index][0], arr[index][1]))
            lista2.append(arr[index])
    return(lista)


# pruebas
print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))
print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_ranges([(1, 2), (2, 3)]))
print(merge_ranges([(1, 5), (2, 3)]))
