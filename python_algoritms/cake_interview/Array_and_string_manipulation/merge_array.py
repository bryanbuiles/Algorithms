"""
concatene dos listas ordenadas con el objetivo
que lalista final tambien esta ordenada
"""


def merge_lists(arr1, arr2):
    size_list = len(arr1) + len(arr2)
    lista = [None] * (size_list)
    flag = 0
    current_index_arr1 = 0
    current_index_arr2 = 0
    for index in range(size_list):
        if arr1[current_index_arr1:] == []:
            lista[index] = arr2[current_index_arr2]
            current_index_arr2 += 1
            flag = 1
            if arr2[current_index_arr2:] == []:
                break
        if arr2[current_index_arr2:] == []:
            lista[index] = arr1[current_index_arr1]
            current_index_arr1 += 1
            flag = 1
            if arr1[current_index_arr1:] == []:
                break
        if flag == 0:
            first_unmerged_alices = arr1[current_index_arr1]
            first_unmerged_mine = arr2[current_index_arr2]
            if first_unmerged_mine < first_unmerged_alices:
                lista[index] = first_unmerged_mine
                current_index_arr2 += 1
            else:
                lista[index] = first_unmerged_alices
                current_index_arr1 += 1
    return lista

# ---------------------------------cake interview example-----------------------------------


def merge_lists(my_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list


my_list = [3, 4, 6, 10, 11, 15, 17, 18, 22, 23]
alices_list = [1, 2, 5, 8, 12, 14, 19, 20, 21]
print(merge_lists(my_list, alices_list))
