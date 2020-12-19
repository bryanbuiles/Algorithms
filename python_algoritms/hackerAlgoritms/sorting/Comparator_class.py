"""
    Title: Sorting: Comparator
    link: https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
    ordenando por el algoritmo de int compare(T o1, T o2)
    Se comparan dos argumentos por orden return -1 if a < b, return 0 if a = b,
    return 1 if a > b
"""

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return ("{} {}".format(self.name, self.score))

    def comparator(a, b):
        if a.score > b.score:
            return -1  # desending order - Primero los mayores por score 100 - 50 -20
        if a.score == b.score:
            if a.name > b.name:  # ascending order by name first example ama, bma
                return 1         # ordenados alafabeticamente
            else:
                return -1
        return 1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

# compare(T o1, T o2)
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
