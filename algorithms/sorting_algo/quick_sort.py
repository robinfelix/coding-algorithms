'''
easy method of implementing quick sort but i guess this increases the space complexity
'''
# def quicksort_space(arr):
#     length = len(arr)
#     if length <= 1:
#         return arr
#     else:
#         pivot = arr.pop()
#
#     arr_lower = []
#     arr_greater = []
#
#     for i in range(len(arr)):
#         if arr[i] < pivot:
#             arr_lower.append(arr[i])
#         else:
#             arr_greater.append(arr[i])
#
#     return quicksort_space(arr_lower) + [pivot] + quicksort_space(arr_greater)
#
# print (quicksort_space(arr))

# def partition(arr):
#     pivot = arr[-1]
#     p_index = 0
#     for i in range(len(arr)-1):
#         if arr[i] <= pivot:
#             arr[i], arr[p_index] = arr[p_index], arr[i]
#             p_index += 1
#     arr[-1], arr[p_index] = arr[p_index], arr[-1]
#     print(arr)
#     return p_index
#
# def quicksort(arr):
#     p_index = partition(arr)
#     print (p_index)
#     quicksort(arr[:p_index])
#     quicksort(arr[p_index:])
#
#
# arr = [12,18,15,21,19,30,4,17]
# quicksort(arr)


def quicksort(arr, left, right):
    '''ref: https://www.youtube.com/watch?v=9KBwdDEwal8 '''
    if left<right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)
    return arr

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while arr[i] < pivot and i < right:
            i += 1

        while arr[j] >= pivot and j > left:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i] , arr[right] = arr[right], arr[i]

    return i


arr =  [22,11,88,66,55,77,33,44]
print (quicksort(arr, 0, len(arr)-1))


