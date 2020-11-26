#!/usr/bin/python3
"""
    barajar los elementos de una lista en oneplace
    este algortimo se llama  shuffle de Fisher-Yates tiempo O(n) espacio O(1)
"""
import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    if len(the_list) < 2:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # Walk through from beginning to end
    for index_que_estamos_mirando in range(len(the_list)):
        # Elija un elemento aleatorio aún no colocado para colocarlo alli
        # (podría ser también el artículo actualmente en ese lugar)
        random_index = get_random(
            index_que_estamos_mirando, last_index_in_the_list)

        # Debe ser un indixe DESPUÉS del indice actual, porque no se puede
        # hacer swap en el mismo indice
        # si son iguales no se cambian, y el numero conserva su actual posicion
        if random_index != index_que_estamos_mirando:
            temp = the_list[index_que_estamos_mirando]
            the_list[index_que_estamos_mirando] = the_list[random_index]
            the_list[random_index] = temp


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
