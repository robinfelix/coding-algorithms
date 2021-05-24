def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    result = []
    for i, val in enumerate(index):
        result.insert(val, nums[i])

    return result

'''
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
'''