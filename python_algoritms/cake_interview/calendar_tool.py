def merge_ranges(arr):
    lista = []
    lista2 = []
    flag = 0
    sorted_arr = sorted(arr)

    for index in range(len(sorted_arr)):
        if sorted_arr[index] in lista2:
            continue
        for elements in sorted_arr[index:]:
            if sorted_arr[index][1] == elements[0] and sorted_arr[index] is not elements:
                if sorted_arr[index] not in lista:
                    if sorted_arr[index][0] < elements[0]:
                        lista.append((sorted_arr[index][0], elements[1]))
                        lista2.append(elements)
                    else:
                        lista.append((elements[0], elements[1]))
                        lista2.append(elements)
                flag = 1
            elif sorted_arr[index][1] > elements[1] and sorted_arr[index] is not elements and sorted_arr[index][1] >= elements[0]:
                if sorted_arr[index] not in lista:
                    if sorted_arr[index][0] < elements[0]:
                        lista.append(
                            (sorted_arr[index][0], sorted_arr[index][1]))
                        lista2.append(elements)
                    else:
                        lista.append((elements[0], sorted_arr[index][1]))
                        lista2.append(elements)
                flag = 1
            elif sorted_arr[index][1] < elements[1] and sorted_arr[index] is not elements and sorted_arr[index][1] >= elements[0]:
                if sorted_arr[index] not in lista:
                    if sorted_arr[index][0] < elements[0]:
                        lista.append((sorted_arr[index][0], elements[1]))
                        lista2.append(elements)
                    else:
                        lista.append((elements[0], elements[1]))
                        lista2.append(elements)
                flag = 1
        if flag == 0:
            lista.append((sorted_arr[index][0], sorted_arr[index][1]))
            lista2.append(sorted_arr[index])
    return(lista)


# pruebas
print(merge_ranges([(2, 6), (3, 5), (7, 9), (1, 10)]))
print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_ranges([(1, 2), (2, 3)]))
print(merge_ranges([(1, 5), (2, 3)]))
