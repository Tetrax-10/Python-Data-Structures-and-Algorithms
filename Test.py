def traverse(node):
    tree = {"value": node["value"]}
    tree.left = null if node.left == null else traverse(node.left)
    tree.right = null if node.right == null else traverse(node.right)
    return tree


def traverse(node):
    tree = {value: node.value}
    tree.left = null if node.left == null else traverse(node.left)
    tree.right = null if node.right == null else traverse(node.right)
    return tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse(node):
    tree = {"value": node["value"]}
    tree["left"] = None if node["left"] == None else traverse(node["left"])
    tree["right"] = None if node["right"] == None else traverse(node["right"])
    return tree


class BST:
    def __init__(self):
        self.root = None

    def printTree(self):
        print("value -->", self.root.value)
        print("left -->", self.root.left)
        print("right -->", self.root.right)

    def insert(self, value):
        newNode = Node(value)
        if(self.root == None):
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if(value < currentNode.value):
                    if(not currentNode.left):
                        currentNode.left = newNode
                        return
                    currentNode = currentNode.left
                else:
                    if(not currentNode.right):
                        currentNode.right = newNode
                        return
                    currentNode = currentNode.right


myTree = BST()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)
# myTree.printTree()
# print(traverse(myTree.root))
print(type(myTree.root))
