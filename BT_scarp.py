class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def inright(self, root):
        if root.val > root.left.val:
            return True


    def isValidBST(self, root, p_val=0) -> bool:
        if root is None:
            return False
        else:
            inleft = self.isValidBST(root.left, root.val)
            inright = self.isValidBST(root.right, root.val)
            print (root.val)
            return  p_val < root.val and p_val > root.val

    #working solution
    def GFG_isvalidBST(self, root, l=None, r=None):
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
        return self.GFG_isvalidBST(root.left, l, root) and \
               self.GFG_isvalidBST(root.right, root, r)

    def existsInTree(self, root, val):
        if root is None:
            return False
        else:
            inleft = self.existsInTree(root.left, val)
            inright = self.existsInTree(root.right, val)
            # print(inleft,inright)
            return root.val == val or inleft or inright

tree = BinaryTree(2)
tree.root.left = Node(1)
# tree.root.left.right = Node(3)
# tree.root.left.left = Node(7)
tree.root.right = Node(3)
# tree.root.right.left = Node(3)
# tree.root.right.right = Node(70)
# tree.root.right.left = Node(15)
# tree.root.right.right = Node(8)
# tree.root.right.right.right = Node(18)
# print (tree.isValidBST(tree.root))

# working solution
print(tree.GFG_isvalidBST(tree.root,None,None))
# print(tree.existsInTree(tree.root,9))

'''
            10
           /  \
        11     9
       /  \   /  \
      7    3 15   8
                   \
                    18
'''
#[5,4,6,null,null,3,7]
# def validator(self, root):
#     if root.left:
#         if root.left.val < root.val:
#             self.validator(root.left)
#         else:
#             return False
#
#     if root.right:
#         if root.right.val > root.val:
#             self.validator(root.right)
#         else:
#             return False
#
#     return True
