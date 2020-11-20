""" Reversar el orden de las palabras completas """


def reverse_words(message):
    reverse(message, len(message), -1, 0)
    spaces = message.count(" ")
    temp2 = -1
    contador = 0
    temp1 = index1 = message.index(" ")
    for times in range(spaces + 1):
        contador_pala = temp1
        reverse(message, contador_pala, temp2, contador)
        temp2 = temp1
        if times + 1 >= spaces:
            temp1 = len(message)
            contador = temp2 + 1
        else:
            index1 = message[temp1 + 1:].index(' ')
            temp1 += index1 + 1
            contador = temp2 + 1
    return(message)


def reverse(message, end_word, start_word, contador):
    for index in range(end_word - 1, start_word, - 1):
        if contador >= index:
            break
        temp = message[contador]
        message[contador] = message[index]
        message[index] = temp
        contador += 1


print(reverse_words(['c', 'a', 'k', 'e', ' ',
                     'p', 'o', 'u', 'n', 'd', ' ',
                     's', 't', 'e', 'a', 'l']))
print(reverse_words(['t', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ',
                     'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd']))
