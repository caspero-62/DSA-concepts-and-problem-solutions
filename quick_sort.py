"""
 Quick Sort Uisng Recursive Method
"""

def partition(input_array, low, high):

    # pivot ==> Element to be placed at right position
    pivot = input_array[high]

    i = low - 1

    for j in range(low, high):
        if input_array[j] < pivot:
            i += 1
            input_array[i], input_array[j] = input_array[j], input_array[i]

    input_array[i + 1], input_array[high] = input_array[high], input_array[i + 1]
    return i + 1


def quick_sort(input_array, high, low=0):

    if low < high:
        pivot = partition(input_array, low, high)
        
        quick_sort(input_array, pivot - 1)
        quick_sort(input_array, high, pivot + 1)

    return input_array


print(quick_sort([10, 80, 30, 90, 40, 50, 70], 6))



