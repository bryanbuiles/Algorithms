"""
    Given a chocolate bar, two children, Lily and Ron, are determining how to share it.
    Each of the squares has an integer on it.

    Lily decides to share a contiguous segment of the bar selected such that:

    The length of the segment matches Ron's birth month, and,
    The sum of the integers on the squares is equal to his birth day.

    You must determine how many ways she can divide the chocolate.
"""


def birthday(s, d, m):
    contador = suma = chocolates = contador2 = 0
    for square in s:
        contador += 1
        suma += square
        if contador == m:
            contador -= 1
            if suma == d:
                chocolates += 1
            suma = suma - s[contador2]
            contador2 += 1
    return chocolates


print(birthday([1, 2, 1, 3, 2], 3, 2))
