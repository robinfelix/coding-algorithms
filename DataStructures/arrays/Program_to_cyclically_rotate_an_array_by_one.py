'''
source : geekforgeek

Following are steps.
1) Store last element in a variable say x.
2) Shift all elements one position ahead.
3) Replace first element of array with x.

Note: The above question can also be solved by using reversal algorithm
'''

arr = [1,2,3,4,5]

temp = arr[-1]
for i in range(-2, -1*(len(arr)+1), -1):
    print (i)
    arr[i+1] = arr[i]

arr[i] = temp
print(arr)