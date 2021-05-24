class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def search(self,val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return  self.right.search(val)
            else:
                return False
    #my approach
    # def find_min(self):
    #     return  self.inorder_traversal()[0]

    # concept approach
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # def delete(self,val):
    #     if val < self.data:
    #         self.left = self.left.delete(val)
    #     elif val > self.data:
    #         self.right = self.right.delete(val)

def build_BST(elements):
    root = BST(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

elements = [17,4,20,9,23,18,34,17]
root = build_BST(elements)
result_sorted = root.inorder_traversal()
#output of BST will be a sorted list with no duplicates ----> important line
print (result_sorted)
print(root.search(4))
print(root.find_min())





