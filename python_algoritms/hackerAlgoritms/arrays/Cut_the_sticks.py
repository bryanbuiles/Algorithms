# Cut the sticks
# https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
    Listasticks = []
    Listasticks.append(len(arr))
    arr = sorted(arr)
    temp = arr[0]
    numbersticks = 0
    for number in arr:
        if temp != number:
            Listasticks.append(len(arr) - numbersticks)
            temp = number
        if temp == number:
            numbersticks += 1
    return Listasticks


print(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]))
