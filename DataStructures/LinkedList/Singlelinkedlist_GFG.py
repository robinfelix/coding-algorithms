class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print(self):
        if self.head is None:
            raise Exception('No element to print')

        itr = self.head
        while itr:
            print(itr.data + '-->')
            itr = itr.next

    def append(self,data):
        if self.head is None:
            self.insert(data)

        itr = self.head
        while itr.next:
            print('in itr')
            itr = itr.next

        node = Node(data)
        itr.next = node


ll = LinkedList()
ll.insert('node0')
ll.append('nodeend')
ll.print()
