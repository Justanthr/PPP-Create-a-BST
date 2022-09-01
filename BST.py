# Part 1: Create a BSTNode class
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


# Part 2: Create a BST class
class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = []


def __str__(self):
    if self.root == None:
        return "The tree is empty"
    else:
        self.output = ""
        self.print_tree(node=self.root)
        return self.output


def __repr__(self):
    if self.root == None:
        return "The tree is empty"
    else:
        self.output = ""
        self.print_tree(node=self.root)
        return self.output


def print_tree(self, node, level=0):
    if node != None:
        self.print_tree(node.right, level + 1)
        self.output += "" * 4 * level + "-->" + str(node.data) + "/n"
        self.print_tree(node.left, level + 1)

# Part 3: Add functionality to your BST class


def add(self, node):
    if type(node) != int and type(node) != BSTNode:
        raise ValueError("You must pass an int or BSTNode")

    if type(node) == int:
        node = BSTNode(node)

    if node.data in self.contents:
        return

    self.add_node(self.root, node)


def add_node(self, cur_node, new_node):
    if new_node > cur_node.data:
        if cur_node.right == None:
            cur_node.right = new_node
            self.contents.append(new_node.data)
            return
        else:
            self.add_node(cur_node.right, new_node)
    else:
        if cur_node.left == None:
            cur_node.left = new_node
            self.contents.append(new_node.data)
            return
        else:
            self.add_node(cur_node.left, new_node)


# test code
node1 = BSTNode(3)
print(node1)  # 3

node2 = BSTNode(4, left=node1)
print(node2)  # 4

node3 = BSTNode()
print(node3)  # None
node3.data = 5
print(node3)  # 5

bst = BST()
print(bst)  # The tree is empty
