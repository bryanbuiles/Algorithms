""" Reversando una lista in a place """


def reverse_list(lista):
    contador = 0
    for index in range(len(lista) - 1, - 1, - 1):
        if contador >= index:
            break
        temp = lista[contador]
        lista[contador] = lista[index]
        lista[index] = temp
        contador += 1
    return(lista)


print(reverse_list(["b", "r", "a", "y", "a", "m"]))
