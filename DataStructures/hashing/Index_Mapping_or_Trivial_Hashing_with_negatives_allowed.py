'''
hashing
create a 2D array
Assign all the values of the hash matrix as 0.
Traverse the given array:
    If the element ele is non negative assign
        hash[ele][0] as 1.
    Else take the absolute value of ele and
         assign hash[ele][1] as 1.
'''



def search(X):
    if X >= 0:
        return arr_2D[X][0] == 1
    X = abs(X)
    return arr_2D[X][1] == 1

def insert(arr):
    for i in range(len(arr)):
        if arr[i] >= 0:
            arr_2D[arr[i]][0] = 1
        else:
            arr_2D[abs(arr[i])][1] = 1
    print(arr_2D)

arr = [-1,3,2,5,10,-9]
MAX = 1000
arr_2D = [[0 for i in range(2)] for j in range(MAX+1)]
print (arr_2D)
insert(arr)
x = 50

print(search(x))