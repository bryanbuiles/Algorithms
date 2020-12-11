""" imprimir un tringualo rectangulo con espacios y "#" """


def staircase(n):
    spaces = n - 1
    num = 1
    for i in range(n):
        print("{}{}".format(spaces * " ", num * "#"))
        spaces -= 1
        num += 1
