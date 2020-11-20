dic = {}


def word_cloud(string):
    index_star = 1
    index_end = flag = 0
    lista = [",", ":", ";", "."]
    letter = (string[0].lower())
    for index in range(1, len(string)):

        if index == (len(string) - 1):
            if string[index] in lista:
                index_end = len(string) - 1
            else:
                index_end = len(string)
            add_word_to_dictionary(string[index_star:index_end])
        if string[index] == ' ':
            if string[index - 1] in lista:
                index_end = index - 1
            else:
                index_end = index
            if index_star == 1 or flag == 1:
                add_word_to_dictionary(
                    letter + string[index_star:index_end])
            else:
                add_word_to_dictionary(string[index_star:index_end])
            index_star = index + 1
            flag = 0
            if string[index_star].isupper() == True and string[index - 1] == ".":
                letter = (string[index_star].lower())
                index_star += 1
                flag = 1
    print(dic)


def add_word_to_dictionary(word):
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1


word_cloud('After beating the eggs, Dana read the next step:')
word_cloud('Add milk and eggs, then add flour and sugar. Pero que hace')
