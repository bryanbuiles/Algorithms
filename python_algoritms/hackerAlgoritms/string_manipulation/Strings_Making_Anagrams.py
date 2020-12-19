def makeAnagram(a, b):
    seta = set()
    setb = set()
    aLen = len(a)
    blen = len(b)
    mayorlen = 0
    if aLen > blen:
        mayorlen = aLen
    else:
        mayorlen = blen

    for index in range(mayorlen):
