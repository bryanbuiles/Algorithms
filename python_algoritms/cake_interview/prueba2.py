def word_cloud(string):
    dic = {}
    index_star = 0
    index_end = 0
    lista = [",", ":", ";"]
    for index in range(len(string)):

        if index == (len(string) - 1):
            if string[index] in lista:
                index_end = len(string) - 1
            else:
                index_end = len(string)
            if string[index_star:index_end] in dic:
                dic[string[index_star:index_end]] += 1
            else:
                dic[string[index_star:index_end]] = 1
        if string[index] == ' ':
            if index > 0 and string[index - 1] in lista:
                index_end = index - 1
            else:
                index_end = index
            if string[index_star:index_end] in dic:
                dic[string[index_star:index_end]] += 1
            else:
                dic[string[index_star:index_end]] = 1
            index_star = index_end + 1

    print(dic)
