class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
#
# print (root.val)
# print(root.left.val)
# print(root.right.val)

##############

def inorder(temp):
    if (not temp): #handle error for Nonetype : None obj has no attribute left
        return

    inorder(temp.left)
    print(temp.val, end=" ")
    inorder(temp.right)


def insert(temp, key):
    if not temp:
        root = Node(key)
        return
    q = []
    q.append(temp)

    # Do level order traversal until we find
    # an empty place.
    count = 0
    while (len(q)):
        temp = q[0]
        q.pop(0)
        count += 1
        print(count)
        if (not temp.left):
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    insert(root, key)
    inorder(root)