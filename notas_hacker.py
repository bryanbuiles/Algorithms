"""
    - cualquier nota por debajo de 38 no se redondea
    - notas > 38 se redondean al multiplo de 5 mas proximo
    - si la diferencia del proximo multiplo de 5 y la nota
        es < 3 la nota se redondea al multiplo de 5
"""


def gradingStudents(grades):
    lista = []
    for notas in grades:
        if notas < 38:
            lista.append(notas)
        else:
            if notas % 5 == 0:
                lista.append(notas)
            else:
                to_cinco = 5 - (notas % 5)
                cinco = notas + to_cinco
                if (cinco - notas) < 3:
                    lista.append(cinco)
                else:
                    lista.append(notas)
    return lista


print(gradingStudents([4, 73, 67, 38, 33]))
