class Node:
    def __init__(self, value):
        self.node = {"value": value, "left": None, "right": None}


def traverse(node, translateToJS=False):
    tree = {"value": node["value"]}
    tree["left"] = None if node["left"] == None else traverse(node["left"])
    tree["right"] = None if node["right"] == None else traverse(node["right"])
    if(not translateToJS):
        return tree
    else:
        return str(tree).replace("None", "null")


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if(self.root == None):
            self.root = newNode.node
        else:
            currentNode = self.root
            while True:
                if(value < currentNode["value"]):
                    if(not currentNode["left"]):
                        currentNode["left"] = newNode.node
                        return
                    currentNode = currentNode["left"]
                else:
                    if(not currentNode["right"]):
                        currentNode["right"] = newNode.node
                        return
                    currentNode = currentNode["right"]


myTree = BST()

myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)

print(traverse(myTree.root, True))
