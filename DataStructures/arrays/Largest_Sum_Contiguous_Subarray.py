arr = [-2,3,2,-1]

def kadenes(arr):
    max_cur = max_global = arr[0]
    for i in range(1,len(arr)):
        # print(max_cur,max_global)
        max_cur = max(arr[i],max_cur+arr[i])
        if max_cur > max_global:
            max_global = max_cur
    return max_global

print (kadenes(arr))