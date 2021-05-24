'''
nice problem add 1 to array , simple reccursive function can solve the problem
'''
def sum(arr, n):
    i = n

    # if array element is less than
    # 9, then simply add 1 to this.
    if (arr[i] < 9):
        arr[i] = arr[i] + 1
        return

    # if array element is greater
    # than 9, replace it with 0
    # and decrement i
    arr[i] = 0
    i -= 1

    # recursive function
    sum(arr, i)


# def addArray(arr):
#     if arr[-1] != 9:
#         arr[-1] += 1
#     else:
#         print ('in else')
#         count = 0
#         for i in range(-1,-1 * len(arr),-1):
#             print(i)
#             if arr[i] == 9:
#                 arr[i] = 0
#                 count += 1
#             else:
#                 arr[i] += 1
#                 break
#
#         if count == len(arr):
#             arr = [1] + [0]*count
#     print(arr)
#
# arr = [9,9,9,9]
# addArray(arr)





