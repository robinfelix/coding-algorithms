arr = [1, 9, 0, 0, 2, 7, 0, 6,]

#single traversal best as of now
def moveZerosToEnd(arr, n):
    # Count of non-zero elements
    pos = 0;

    # Traverse the array. If arr[i] is non-zero, then
    # swap the element at index 'count' with the
    # element at index 'i'
    for i in range(0, n):
        if (arr[i] != 0):
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
            print (i , pos, arr)
    # print(arr)
moveZerosToEnd(arr, len(arr))
#
# def pushZerosToEnd(arr, n):
#     count = 0  # Count of non-zero elements
#
#     # Traverse the array. If element
#     # encountered is non-zero, then
#     # replace the element at index
#     # 'count' with this element
#     for i in range(n):
#         if arr[i] != 0:
#             # here count is incremented
#             arr[count] = arr[i]
#             count += 1
#     print (arr)
#     # Now all non-zero elements have been
#     # shifted to front and 'count' is set
#     # as index of first 0. Make all
#     # elements 0 from count to end.
#     while count < n:
#         arr[count] = 0
#         count += 1
#
#
# # Driver code
# arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
# n = len(arr)
# pushZerosToEnd(arr, n)
# print("Array after pushing all zeros to end of array:")
# print(arr)

# my approach
# def count(a):
#     c = 0
#     if a == 0:
#         c = c + 1
#     return c
#
# def arrange(arr):
#     print("dsdsd")
#     arr.sort(key=count)
#     print(arr)
# arrange(arr)

