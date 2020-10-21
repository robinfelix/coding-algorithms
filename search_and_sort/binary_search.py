#author : robinfelix
#wow 1st run itself was sucessful and my code is much is simpler than in tutorial
# (emote) - feeling motivated  ##ignore social media practice :P
#successfully code attaching solution for future reference
# doubt:  can we perform binary search in unsorted array ?  (rotated array) # i know it doesnt make sense
'''
catch here is array need to be sorted first to do binary search
https://www.youtube.com/watch?v=T2sFYY-fT5o

We basically ignore half of the elements just after one comparison.

Compare x with the middle element.
If x matches with middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
Else (x is smaller) recur for the left half.

its a log(n)
'''

arr = [2,5,8,12,16,23,38,56,72,91]
x = 23
# x = 175

def bin_search(arr, x):
    mid_index = int(len(arr)/2)
    print (mid_index)
    middle = arr[mid_index]
    if middle == x:
        return mid_index
    elif x > middle:
        bin_search(arr[middle:],x)
    elif x < middle:
        bin_search(arr[:middle],x)


print("index",bin_search(arr,x))