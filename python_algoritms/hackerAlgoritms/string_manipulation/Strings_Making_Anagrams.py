"""
    Strings: Making Anagrams
    https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
    Hacer anagramas apartir de dos strings
"""


def makeAnagram(a, b):
    Diclettera = {}
    contador = sumaLettersa = 0
    for letter in a:
        if letter in Diclettera:
            Diclettera[letter] += 1
        else:
            Diclettera[letter] = 1
        sumaLettersa += 1
    for letterb in b:
        if letterb in Diclettera:
            if Diclettera[letterb] == 0:
                contador += 1
            else:
                Diclettera[letterb] = Diclettera[letterb] - 1
                sumaLettersa -= 1
        else:
            contador += 1
    contador += sumaLettersa
    return contador


a = "cde"
b = "abc"
a = "cde"
b = "def"
print(makeAnagram(a, b))
