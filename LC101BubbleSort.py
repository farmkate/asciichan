# Sorts a list using bubble sort.
# Does not alter the original list but returns a sorted version of it.
#from test import testEqual

def insert(sorted_list, num):
    new_idx = 0
    while new_idx < len(sorted_list) and num > sorted_list[new_idx]:
        new_idx += 1
    new_sorted_list = sorted_list[:new_idx] + [num] + sorted_list[new_idx:]
    return new_sorted_list



def bubble_sort(lst):
    # TODO your code here
    is_sorted = False
    sorted_list = lst[:]

    while is_sorted == False:
            nswaps = 0  #number of swaps made
            for i in range(len(sorted_list)-1):
                if sorted_list[i] > sorted_list[i + 1]:
                    sorted_list.insert(i, sorted_list.pop(i+1))
                    nswaps += 1
            if nswaps == 0:
                is_sorted = True
    return sorted_list

list = [55, 66, 22, 59, 88, 1546, 1, 3, 1]


print(insert(bubble_sort(list), 54))
#testEqual(insert([2,3], 1), [1,2,3])
