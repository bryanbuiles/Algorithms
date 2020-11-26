"""
    verificar si cualquier
    combinacion de una palabra puede ser un palindromo
    O(n) time complexity
"""
import unittest


def palindrome(string):
    dic = {}
    flag = contador1 = 0
    for letter in string:
        contador = 0
        if letter in dic:
            contador += dic[letter] + 1
            dic[letter] = contador
        else:
            dic[letter] = 1
    for palindrome in string:
        if len(string) % 2 == 0:
            if dic[palindrome] % 2 != 0:
                return False
            flag = 1
        else:
            if dic[palindrome] % 2 != 0:
                contador1 += 1

    if flag == 1:
        return True
    if contador1 >= 2:
        return False
    return True

# cake version


def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1


class TestPalindrome(unittest.TestCase):

    def test_case1(self):
        current = palindrome("civicv")
        expect = True
        self.assertEqual(current, expect)

    def test_case2(self):
        current = palindrome("ccvicc")
        expect = False
        self.assertEqual(current, expect)

    def test_case3(self):
        current = palindrome("ccvcc")
        expect = True
        self.assertEqual(current, expect)

    def test_case4(self):
        current = palindrome("civic")
        expect = True
        self.assertEqual(current, expect)

    def test_case5(self):
        current = palindrome("ivicc")
        expect = True
        self.assertEqual(current, expect)

    def test_case6(self):
        current = palindrome("civil")
        expect = False
        self.assertEqual(current, expect)


if __name__ == '__main__':
    unittest.main()
