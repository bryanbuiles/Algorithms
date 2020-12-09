# https://www.hackerrank.com/challenges/queens-attack-2/problem
# Queen's Attack II

def queensAttack(n, k, r_q, c_q, obstacles):
    lista = [r_q, c_q]
    r_q -= 1
    tempr = r_q
    c_q -= 1
    tempc = c_q
    contador = 0
    # horizontal right
    for squares in range(0, n):
        if tempc >= n - 1:
            break
        tempc += 1
        lista[1] = tempc + 1
        if lista in obstacles:
            break
        contador += 1
    # horizontal left
    tempc = c_q
    for squares in range(0, n):
        if tempc <= 0:
            break
        tempc -= 1
        lista[1] = tempc + 1
        if lista in obstacles:
            break
        contador += 1
    # vertical right up
    tempc = c_q
    for squares in range(0, n):
        if tempc >= n - 1 or tempr >= n - 1:
            break
        tempr += 1
        tempc += 1
        lista[0] = tempr + 1
        lista[1] = tempc + 1
        if lista in obstacles:
            break
        contador += 1
    # vertical down and left
    tempc = c_q
    tempr = r_q
    for squares in range(0, n):
        if tempc <= 0 or tempr <= 0:
            break
        tempr -= 1
        tempc -= 1
        lista[0] = tempr + 1
        lista[1] = tempc + 1
        if lista in obstacles:
            break
        contador += 1
    # vertical up left
    tempc = c_q
    tempr = r_q
    for squares in range(0, n):
        if tempc <= 0 or tempr >= n - 1:
            break
        tempr += 1
        tempc -= 1
        lista[0] = tempr + 1
        lista[1] = tempc + 1
        if lista in obstacles:
            break
        contador += 1
    # vertical down and right
    tempc = c_q
    tempr = r_q
    for squares in range(0, n):
        if tempc >= n - 1 or tempr <= 0:
            break
        tempr -= 1
        tempc += 1
        lista[0] = tempr + 1
        lista[1] = tempc + 1
        if lista in obstacles:
            break
        contador += 1
    # vertical up
    tempc = c_q
    tempr = r_q
    for squares in range(0, n):
        if tempr >= n - 1:
            break
        tempr += 1
        lista[0] = tempr + 1
        lista[1] = tempc + 1
        if lista in obstacles:
            break
        contador += 1
    # vertical down
    tempr = r_q
    for squares in range(0, n):
        if tempr <= 0:
            break
        tempr -= 1
        lista[0] = tempr + 1
        if lista in obstacles:
            break
        contador += 1
    return contador


lista = [[5, 5], [4, 2], [2, 3]]
print(queensAttack(5, 3, 4, 3, lista))
# lista = []
# print(queensAttack(4, 0, 4, 4, lista))
