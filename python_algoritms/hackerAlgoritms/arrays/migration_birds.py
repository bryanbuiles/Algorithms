"""
    Each bird has a id identified with a integer.
    Your task is to print the type number of that bird that is more commoon and if
    two or more types of birds are equally common, choose the type with the smallest ID number.
"""


def migratoryBirds(arr):
    dic = {}
    for integers in arr:
        contador = 0
        if integers in dic:
            contador += dic[integers] + 1
            dic[integers] = contador
        else:
            dic[integers] = 1
    more_common_bird = dic[arr[0]]
    less_index_bird = arr[0]
    for key, value in dic.items():
        if value == more_common_bird and less_index_bird > key:
            print("key {} value {}".format(key, value))
            less_index_bird = key
        if value > more_common_bird:
            more_common_bird = value
            less_index_bird = key
    return less_index_bird


print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
# respuesta 3 porque es el numero que mas se repite en la lista
# y ademas tiene el menor indixe
