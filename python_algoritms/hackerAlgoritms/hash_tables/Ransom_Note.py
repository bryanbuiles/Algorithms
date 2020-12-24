#!/bin/python3
"""
    Hash Tables: Ransom Note
    https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
    Si es posible formar el mensaje con las palabras de la revista
"""


def checkMagazine(magazine, note):
    dic_magazine = {}
    flag = 0
    for index in range(len(magazine)):
        word = magazine[index]
        value = dic_magazine.get(word, 0)
        dic_magazine[word] = value + 1

    for words_note in note:
        value = dic_magazine.get(words_note)
        if value == None or value == 0:
            print("No")
            flag = 1
            break
        else:
            dic_magazine[words_note] -= 1
    if flag != 1:
        print("Yes")


magazine = ['two', 'times', 'three', 'is', 'not', 'four']
note = ['two', 'times', 'two', 'is', 'four']
magazine = ["o", "l", "x", "imjaw", "bee", "khmla",
            "v", "o", "v", "o", "imjaw", "l", "khmla", "imjaw"]
note = ["imjaw", "l", "khmla", "x", "imjaw", "o", "l", "l",
        "o", "khmla", "v", "bee", "o", "o", "imjaw", "imjaw", "o"]
checkMagazine(magazine, note)
