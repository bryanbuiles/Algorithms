def nonDivisibleSubset(k, s):
    lista = []
    for index in range(0, len(s)):
        conjunto = set()
        conjunto.add(s[index])
        for index_inside in range(0, len(s)):
            if s[index] != s[index_inside] and (s[index] + s[index_inside]) % k != 0:
                conjunto.add(s[index_inside])
        lista.append(conjunto)
    print(lista)


print(nonDivisibleSubset(4, [19, 10, 12, 24, 25, 22]))
