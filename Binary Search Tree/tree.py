""" This Code is Slightly Modified (more advanced) than the javascript code to fix some bugs that happens in
 original code. eg: without inserting any values if you call lookup it causes error.
 here it returns False."""


class Node:
    def __init__(self, value=None):
        if(not value):
            self.node = None
        else:
            self.node = {"value": value, "left": None, "right": None}


def traverse(node, translateToJS=False):
    if(node == False or node == None):
        return node

    tree = {"value": node["value"]}
    tree["left"] = None if node["left"] == None else traverse(node["left"])
    tree["right"] = None if node["right"] == None else traverse(node["right"])

    if(not translateToJS):
        return tree
    else:
        return str(tree).replace("None", "null")


class BST:
    def __init__(self):
        newNode = Node()
        self.root = newNode.node

    def insert(self, value):
        newNode = Node(value)

        if(self.root == None):
            self.root = newNode.node
        else:
            currentNode = self.root
            # travells to the leaf node (left or right according to the value)
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

    def lookup(self, value):
        if(not self.root):
            return False
        currentNode = self.root
        while(currentNode):
            if(value < currentNode["value"]):
                currentNode = currentNode["left"]
            elif(value > currentNode["value"]):
                currentNode = currentNode["right"]
            elif(value == currentNode["value"]):
                return currentNode
        return False  # if specified value is not in the node then return False


myTree = BST()

myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)

# print(traverse(myTree.root, True))
print(traverse(myTree.lookup(170), True))
# print(traverse(myTree.lookup(0), True))


#            9
#       4         20
#    1    6    15   170
