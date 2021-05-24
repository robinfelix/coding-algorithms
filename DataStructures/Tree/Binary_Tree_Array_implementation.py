tree = [None] * 10


def root(data):
    if tree[0] != None:
        print("root already present")
    else:
        tree[0] = data


def set_left(data, parent):
    if tree[parent] is not None:
        tree[(2 * parent) + 1] = data
    else:
        print("doent have parent at pos : ", (2 * parent) + 1)


def set_right(data, parent):
    if tree[parent] is not None:
        tree[(2 * parent) + 2] = data
    else:
        print("doent have parent at pos : ", (2 * parent) + 2)


def print_tree():
    print(tree)


root('A')
set_left('B', 0)
set_right('C',0)
set_right('D',0)
print_tree()