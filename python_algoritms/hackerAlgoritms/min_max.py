""" calcular la maxima suma en una array de 5 integers """
from functools import reduce


def miniMaxSum(arr):
    maxvalue = max(arr)
    minvalue = min(arr)
    sum = reduce(lambda x, y: x + y, arr)
    resultmax = sum - minvalue
    resultmin = sum - maxvalue
    print("{} {}".format(resultmin, resultmax))


miniMaxSum([1, 2, 3, 4, 5])
