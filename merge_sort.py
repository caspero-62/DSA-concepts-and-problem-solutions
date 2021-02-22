def merge_sort(input_array):
    if len(input_array) > 1:
        mid = len(input_array) // 2
        
        input_array1 = input_array[:mid]
        input_array2 = input_array[mid:]
        
        merge_sort(input_array1)
        merge_sort(input_array2)

        # Create indexes for the 1st sorted array, second and also main array
        i = j = k = 0

        while i < len(input_array1) and j < len(input_array2):
            if input_array1[i] < input_array2[j]:
                input_array[k] = input_array1[i]
                i += 1
            else:
                input_array[k] = input_array2[j]
                j += 1
            k += 1

        while i < len(input_array1):
            input_array[k] = input_array1[i]
            i += 1
            k += 1

        while j < len(input_array2):
            input_array[k] = input_array2[j]
            j += 1
            k += 1

    return input_array

print(merge_sort([1,2,5,7,3,4,4]))