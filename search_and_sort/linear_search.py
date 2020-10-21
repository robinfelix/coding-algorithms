#author : robinfelix
#successfully code attaching solution for future reference
'''
A simple approach is to do a linear search, i.e

Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.

complexity : n
'''

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
# x = 110
x = 175

def lin_search(arr,x):
    for index, val in enumerate(arr):
        if val == x:
            return index
    return -1

print ("Element x is present at index {0}".format(lin_search( arr, x)))