# ACM ICPC Team
# https://www.hackerrank.com/challenges/acm-icpc-team/problem
# Calcular la combinacion de grupos mejor preparados - usa conjuntos

def acmTeam(topic):
    lista_set = []
    max_len = contador = 0
    # Primer loop para sacar los indices cuando es = '1'
    for index_out in range(0, len(topic)):
        main_set = set()
        for indes_in in range(0, len(topic[index_out])):
            if topic[index_out][indes_in] == '1':
                main_set.add(indes_in + 1)
        lista_set.append(main_set)

    # para comparar los diferentes set y ver cual es mas grande
    for sets in range(0, len(lista_set)):
        set_ref = lista_set[sets]
        for sets_in in range(sets, len(lista_set)):
            new_set = lista_set[sets_in].union(set_ref)
            len_set = len(new_set)
            if len_set == max_len:
                contador += 1
            if len_set > max_len:
                contador = 1
                max_len = len_set
    return max_len, contador


lista = ["10101", "11100", "11010", "00101"]
print(acmTeam(lista))
