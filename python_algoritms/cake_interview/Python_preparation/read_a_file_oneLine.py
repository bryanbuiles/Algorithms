""" Count Capital Letters

    Escribir en una linea y que sea entendible el numero de letras en el
    mayusculas al abrir un archivo.e

    EL codigo debe servir incluso si el archivo es muy grande para la memoria
    osea no metodo read()
"""

with open(SOME_LARGE_FILE) as fh:
    count = sum(character.isupper() for line in fh for character in line)
