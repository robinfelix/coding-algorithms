arr = [12, 11, 13, 5, 6, 7]

def merge_divide(arr):
    # print(arr)
    left, right = [],[]
    mid = int(len(arr)/2)
    if len(arr) > 1:
        left = arr[:mid]
        right = arr[mid:]
        merge_divide(left)
        merge_divide(right)
        # print ("done divide left", left)
        # print ("done divide right", right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    print(arr)
    # return left,right

# def merge_sort(arr):
#     left, right = merge_divide(arr)
#     print("left    : ", left)
#     print("right   : ", right)

# merge_sort(arr)
merge_divide(arr)