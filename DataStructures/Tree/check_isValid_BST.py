'''
optimal solution
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, l=None, r=None) -> bool:
        if root == None:
            return True

            # if left node exist then check it has
            # correct data or not i.e. left node's data
            # should be less than root's data
        if (l != None and root.val <= l.val):
            return False

            # if right node exist then check it has
            # correct data or not i.e. right node's data
            # should be greater than root's data
        if (r != None and root.val >= r.val):
            return False

            # check recursively for every node.
        return self.isValidBST(root.left, l, root) and \
               self.isValidBST(root.right, root, r)





