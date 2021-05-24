# arr = [90, 15, 10, 7, 12, 2, 7, 3]
#True cases
# arr = [90, 15, 10, 7, 12, 2]
arr = [100, 40, 50, 10, 15, 50, 40]
# arr = [97, 46, 37, 12, 3, 7, 31, 6, 9]
# arr = [90, 15, 10, 7, 12, 2]
# arr = [93, 15, 87, 7, 15, 5]
# arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
# arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# arr = [100, 19, 36, 17, 3, 25, 1, 2, 7]
# arr = [5, 5, 5, 5, 5, 5, 5, 5]
# arr = [97]

# False cases
# arr = [4, 5, 5, 5, 5, 5, 5, 5]
# arr = [90, 15, 10, 7, 12, 11]
# arr = [1, 2, 3, 4, 5]
# arr = [4, 8, 15, 16, 23, 42]
# arr = [2, 1, 3]
# this method check the child node from bottom and make sure its root node is greater than it
# def isheap(arr):
#     node = arr[len(arr)-1]
#     print(node)
#
#     for i in range(1,len(arr)):
#         print(arr[i])
#         if arr[i] <= arr[int((i-1)/2)]:
#             continue
#         else:
#             return False
#     return True

# this method check that every node's left and right node is lesser than its value
def isheap(arr):
    # l_child = (2 * i) + 1
    # r_child = (2 * i) + 2
    for i in range(len(arr)):
        if (2 * i) + 2 <= len(arr): #checking of left bound is enough i guess
        # if (2 * i) + 1 < len(arr) and (2 * i) + 2 < len(arr): # checked both left and right bound
            if arr[i] >= arr[(2 * i) + 1] and arr[i] >= arr[(2 * i) + 2]:
                print (arr[i])
                continue
            else:
                return False
    return True

print("Does the above arr is in max heap : ", isheap(arr))
