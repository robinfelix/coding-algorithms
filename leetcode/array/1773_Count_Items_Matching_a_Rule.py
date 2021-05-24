'''
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
'''
#best solution
def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
    # print (item_list[{"type":0, "color":1, "name":2}[ruleKey])
    return sum(item_list[{"type":0, "color":1, "name":2}[ruleKey]] == ruleValue for item_list in items)

#my soljution

# def countMatches(items, ruleKey: str, ruleValue: str) -> int:
#     from collections import Counter
#     ref = {'type': 0, 'color': 1, 'name': 2}
#     y = ref[ruleKey]
#     data = []
#     for i in range(len(items)):
#         data.append(items[i][y])
#
#     c = Counter(data)
#     return c[ruleValue]


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print (countMatches(items, ruleKey, ruleValue))