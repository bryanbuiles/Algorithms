"""
    Contruir un algoritmo que permita al usuario ver dos peliculas
    en un vuelo
"""


def movie_flight(movie_lengths, flight_length):
    dic = {}
    flag = 0

    for index in range(len(movie_lengths)):
        total_time_movie = flight_length - movie_lengths[index]
        if total_time_movie in dic:
            flag = 1
        dic[movie_lengths[index]] = "movie" + str(index)
        if flag == 1:
            return (dic[movie_lengths[index]], dic[total_time_movie])
    return "no movies found"


lista2 = [120, 133, 160, 150, 130, 152, 150]
lista = [120, 133, 160, 142, 130, 152]
flight = 300
flight2 = 250

print(movie_flight(lista, flight2))

# ----------------------version interview cake---------------------------


def movie_flight_cake(movie_lengths, flight_length):
    set_movies = set()

    for movies in movie_lengths:
        total_time_movie = flight_length - movies
        if total_time_movie in set_movies:
            return (True)
        set_movies.add(movies)
    return "no movies found"
