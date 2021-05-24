class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)



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
