"""
========================= BUBBLE SORT METHOD USING A COMPARISON ARRAY ================================ 
"""

def bubble_sort(input_array):
    array_is_sorted = False
    while not array_is_sorted:
        comp_array = input_array[:]
        for i in range(1, len(input_array)):
            if input_array[i] < input_array[i-1]:
                input_array[i], input_array[i-1] = input_array[i-1], input_array[i] 
        if comp_array == input_array:
            array_is_sorted = True
    return input_array

print(bubble_sort([1, 3, 2, 9, 8, 5, 6, 4, 7]))

"""
========================= OR USING TWO FOR LOOPS ================================ 
"""

def bubble_sort2(input_array):
    for i in range(1, len(input_array)):
        flag = 0

        for j in range(1, len(input_array)):
           if input_array[j] < input_array[j-1]:
                input_array[j], input_array[j-1] = input_array[j-1], input_array[j]
                flag = 1 

        if flag == 0:
            break

    return input_array

print(bubble_sort2([1, 3, 2, 9, 8, 5, 6, 4, 7]))