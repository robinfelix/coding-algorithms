'''
Source : geeksforgeeks
my solution
1) find min element and its position in arr
2) find no of elements from pos to len(arr) --> pivot array
3) rotate anticlockwise and pass it to binary search

better solution:
Input arr[] = {3, 4, 5, 1, 2}
Element to Search = 1
  1) Find out pivot point and divide the array in two
      sub-arrays. (pivot = 2) /*Index of 5*/
  2) Now call binary search for one of the two sub-arrays.
      (a) If element is greater than 0th element then
             search in left array
      (b) Else Search in right array
          (1 will go in else as 1 < 0th element(3))
  3) If element is found in selected sub-array then return index
     Else return -1.
'''

#my solution
def mysolution():
    min_ele = min(arr)
    minpos = arr.index(min_ele)
    pivot_arr = arr[minpos:len(arr)]
    reg_arr = arr[:minpos]
    result = pivot_arr + reg_arr
    print (result)

#better solution
# def binarysearch(t_arr, x):
#     print(t_arr)
#     mid_idx = int(len(t_arr)/2)
#     middle = t_arr[mid_idx]
#     if middle == x:
#         return mid_idx
#     elif middle > x:
#         binarysearch(t_arr[:mid_idx], x)
#     elif middle < x:
#         binarysearch(t_arr[mid_idx:], x)
#     return -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1

def bettersolution(arr, x):
    min_ele = min(arr)
    minpos = arr.index(min_ele)
    pivot_arr = arr[minpos:len(arr)]
    reg_arr = arr[:minpos]
    print("pivor arr", pivot_arr)
    print("regular arr", reg_arr)
    if reg_arr[0] == x:
        return 0
    elif reg_arr[0] > x:
        s_idx = binary_search(pivot_arr, 0, len(pivot_arr), x)
        s_idx = s_idx + len(reg_arr)
    elif reg_arr[0] < x:
        s_idx = binary_search(reg_arr, 0, len(reg_arr), x)
    else:
        s_idx = -1

    return (s_idx)

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
x = 5
print ("given arr ", arr)
print (bettersolution(arr, x))
