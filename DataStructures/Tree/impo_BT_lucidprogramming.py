''' source : Best explanation on lucid programming channel

'''


class Queue(object):
    def __init__(self):
        self.array = []

    def enqueue(self, item):
        self.array.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0

    def peek(self):
        if not self.is_empty():
            return self.array[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.array)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # Breath First Search technique
    def pre_order_traversal(self, start, traversal):
        '''Root -> Left -> Right'''
        if start:
            traversal += str(start.value) + '--'
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    # Breath First Search technique
    def in_order_traversal(self, start, traversal):
        '''Left -> Root -> Right'''
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal += str(start.value) + '--'
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    # Breath First Search technique
    def post_order_traversal(self, start, traversal):
        '''Left -> Right -> Root'''
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal += str(start.value) + '--'
        return traversal

    def level_order_traversal(self, start):
        '''print all nodes for each level starts from root
        10--11--9--7--3--15--8--18-- '''
        if start is None:
            return

        traversal = ''
        queue = Queue()
        queue.enqueue(start)
        while len(queue) > 0:
            traversal += str(queue.peek()) + '--'
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal


'''
            10
           /  \
        11     9
       /  \   /  \
      7    3 15   8
                   \
                    18
'''

tree = BinaryTree(10)
tree.root.left = Node(11)
tree.root.left.right = Node(3)
tree.root.left.left = Node(7)
tree.root.right = Node(9)
tree.root.right.left = Node(15)
tree.root.right.right = Node(8)
tree.root.right.right.right = Node(18)

print ("preorder : ",tree.pre_order_traversal(tree.root, traversal = ''))
print ("Inorder : ",tree.in_order_traversal(tree.root, traversal = ''))
print ("preorder : ",tree.post_order_traversal(tree.root, traversal = ''))
print("level order traversal : ", tree.level_order_traversal(tree.root))
