class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def existsInTree(self, root, search_val, node):
        if root is None:
            return False
        else:
            inleft = self.existsInTree(root.left, search_val, root.value)
            inright = self.existsInTree(root.right, search_val, root.value)
            # print(inleft,inright)
            return root.value == search_val or inleft or inright

tree = BinaryTree(10)
tree.root.left = Node(11)
# tree.root.left.right = Node(3)
# tree.root.left.left = Node(7)
tree.root.right = Node(9)
# tree.root.right.left = Node(15)
# tree.root.right.right = Node(8)
# tree.root.right.right.right = Node(18)

print(tree.existsInTree(tree.root,10, tree.root.value))

'''
            10
           /  \
        11     9
       /  \   /  \
      7    3 15   8
                   \
                    18
'''