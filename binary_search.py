"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

import math

def binary_search(input_array, value):
    """Your code goes here."""
    index = 0
    new_array_sort = input_array
    # find the index of middle element
    def middle_index(array_mid_index):
        return int(math.floor((len(array_mid_index) - 1)/2))
    # find the element at middle of array
    def middle_number(array_mid_index):
        return array_mid_index[int(math.floor((len(array_mid_index) - 1)/2))]
    # start index at middle of array
    index += middle_index(new_array_sort)
    # while array is not empty, do something beautiful
    while new_array_sort:
        if value == middle_number(new_array_sort):
            if new_array_sort == input_array:
                return index
            return index + middle_index(new_array_sort)
        elif value > middle_number(new_array_sort):
            new_array_sort = new_array_sort[middle_index(new_array_sort) + 1:]
            index += middle_index(new_array_sort)
        else:
            new_array_sort = new_array_sort[:middle_index(new_array_sort)]
            index -= middle_index(new_array_sort)
    # return -1 if number not found in array
    return -1

test_list = [1,3,9,11]
test_val1 = 25
test_val2 = 15
test_val3 = 3

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val3))