
'''my approach but not suitable for interview i guess'''
def kthsmallestnum(arr,k):
    arr.sort()
    print (arr[k-1])

arr = [7, 10, 4, 3, 20, 15]
k = 3
kthsmallestnum(arr,k)
'''
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.
'''




