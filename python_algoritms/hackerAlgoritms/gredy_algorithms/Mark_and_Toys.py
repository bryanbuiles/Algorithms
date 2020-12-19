"""
    Mark and Toys
    https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
"""


def maximumToys(prices, k):
    contador = suma = 0
    sorted_list = sorted(prices)
    for i in sorted_list:
        if suma + i <= k:
            suma += i
            contador += 1
        else:
            break
    return contador


lista = [1, 12, 5, 111, 200, 1000, 10]
k = 50
print(maximumToys(lista, k))
