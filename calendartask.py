""" Calendar tool with = O(nlogn) """


def merge_ranges(meetings):
    lista = []
    # Sort by start time
    sorted_meetings = sorted(meetings)
    star = sorted_meetings[0][0]
    end = sorted_meetings[0][1]

    for current_star, current_end in sorted_meetings:
        if current_star > end:
            lista.append((star, end))
            star = current_star
            end = current_end
        elif current_end >= end:
            end = current_end
    if (star, end) not in lista:
        lista.append((star, end))
    return lista


print(merge_ranges([(2, 6), (3, 5), (7, 9), (1, 10)]))
print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_ranges([(1, 2), (2, 3)]))
print(merge_ranges([(1, 5), (2, 3)]))
