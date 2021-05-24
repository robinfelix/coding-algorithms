'''
O(n^2)
selection sort can be used when min number of swaps is required

'''

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        j = i + 1
        # print(len(arr[j:]))
        while j < len(arr):
            if arr[min_idx] > arr[j]:
                min_idx = j
                j += 1
            else:
                j += 1

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [17,2,1,9,8,7,13]
print (selection_sort(arr))
