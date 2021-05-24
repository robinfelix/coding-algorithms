A = [1, 2, 3, 4, 5, 6]
#best and easy approach pythonic way
print (A[::-1])
#1st approach
# def reverseArray(arr, start, end):
#     while start < end:
#         print(arr)
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#
# reverseArray(A,0,len(A)-1)
