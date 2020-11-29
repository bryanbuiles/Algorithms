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

############# cake interview Solution #####################################
def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backward

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index += 1
        right_index -= 1
