arr = [1, 5, 3, 7, 9]
x = 12

#O(n^2) worst approach
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] + arr[j]) == x:
            print ('({0}, {1}) {2}'.format(arr[i],arr[j],x))

#O(n) best of all
for i in range(len(arr)):
    diff = x-arr[i]
    if diff in arr[i+1:]:
        print (diff, arr[i])

#using combinations
from itertools import combinations

def findPairs(lst, K):
    res = []
    for var in combinations(lst, 2):
        if var[0] + var[1] == K:
            res.append((var[0], var[1]))
    return res
# Driver code
lst = [1, 5, 3, 7, 9]
K = 12
print(findPairs(lst, K))

#Method  # 4 : itertools.combinations (Efficient method)

# Python3 program to find all pairs in
# a list of integers with given sum
from itertools import combinations
def findPairs(lst, K):
    return [pair for pair in combinations(lst, 2) if sum(pair) == K]

# Driver code
lst = [1, 5, 3, 7, 9]
K = 12
print(findPairs(lst, K))