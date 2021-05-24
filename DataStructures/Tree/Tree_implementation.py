class Tree:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def addchild(self, child):
        self.children.append(child)
        # self.parent = self

    def printtree(self):
        print (self.data)
        for child in self.children:
            print(child.data)

def buildtree():
    root = Tree("electronics")

    laptop = Tree('laptop')
    mobiles = Tree('mobiles')
    root.addchild(laptop)
    root.addchild(mobiles)



    root.printtree()


buildtree()
