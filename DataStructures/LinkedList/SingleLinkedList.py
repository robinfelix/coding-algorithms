class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def printll(self):
        if self.head is None:
            print('No elements in LinkedList')

        itr = self.head
        while itr:
            print(itr.data + '--->')
            itr = itr.next

    def insert_at_end(self, data):
        itr = self.head
        if itr is None:
            print ("No elements at LinkedList Inserting at front")
            self.insert_at_beginning(data)
            return

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def lengthll(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def deletell(self, index):
        if index < 0 and index >= self.lengthll():
            print ("Invalid index")
            return

        if index == 0:
            self.head = self.head.next # Important catch here LL is 1

        itr = self.head
        count = 0
        while count <= index-1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    # TODO : need to work on this
    def insert_at(self, index, data):
        itr = self.head
        print("current node : ",itr.data)
        count = 0
        while count < index-1:
            itr = itr.next
            count += 1
        # itr.next.next
        itr.next = Node(data, itr.next)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning('node3')
    # ll.insert_at_beginning('node1')
    ll.insert_at_beginning('node2')
    ll.insert_at_beginning('node0')
    # ll.insert_at_end('endnode1')
    ll.printll()
    ll.deletell(0)
    # print('*'*20 + '  After delting' )
    # ll.printll()
    print('*'*20 + '  After inserting' )
    ll.insert_at(2,'somathing')
    ll.printll()
    print ("length : ",ll.lengthll())