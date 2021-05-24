'''
famous algorithm for finding continoius sub arrray
'''

arr = [-2,3,2,-1]


# for fun i am trying brute force
temp = []
#below for loop game me all possible combinations of arr taking max sum will do the work
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         print ( arr[i:j+1])
# print(temp)

# best solution is kadens algorithm
def kadenes(arr):
    max_cur = max_global = arr[0]
    for i in range(1,len(arr)):
        print('@@',i,max_cur+arr[i])
        max_cur = max(arr[i],max_cur+arr[i]) #important lineeeee
        if max_cur > max_global:
            max_global = max_cur
    return max_global

print (kadenes(arr))