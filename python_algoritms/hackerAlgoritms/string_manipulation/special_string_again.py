#!/bin/python3

def substrCount(n, s):
    lista_letters = []
    contador = flag = contadorint = 0
    for letter in range(1, n):
        for substring in range(n - letter):
            flag = 0
            lista_letters = s[substring:substring+letter+1]
            lenStrings = len(lista_letters)
            for index in range(lenStrings):
                if lenStrings % 2 == 0 and lista_letters[0] != lista_letters[index]:
                    flag = 1
                if lenStrings % 2 != 0:
                    if lista_letters[lenStrings//2] != lista_letters[0] and lista_letters[0] == lista_letters[index]:
                        flag = 1
                        contadorint += 1
                    if lista_letters[0] != lista_letters[index]:
                        flag = 1

            if flag == 0 or contadorint == (lenStrings - 1):
                contador += 1
            contadorint = 0
    return n + contador


n = 7
s = "abcbaba"
n = 4
s = "aaaa"
print(substrCount(n, s))
