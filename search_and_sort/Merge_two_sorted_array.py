## Merge two sorted array

arr1 = [1,2,5,6]
arr2 = [3,4,7,8]
arr3 = []
i = j = k = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1
k += 1

while i < len(arr1):
    arr3.append(arr1[i])
    i +=1
    k +=1

while j < len(arr2):
    arr3.append(arr2[j])
    j +=1
    k +=1

print(arr3)