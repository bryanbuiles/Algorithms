""" numero de cifras decimales de 6 """


def plusMinus(arr):
    positive = cero = negative = 0
    elements = len(arr)
    for number in arr:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            cero += 1
    print("{0:.6f}".format(positive/elements))
    print("{0:.6f}".format(negative/elements))
    print("{0:.6f}".format(cero/elements))
