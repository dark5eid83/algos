# You are given a Node class that has a name and an array of optional children nodes
# when put together, nodes form a tree-like structure.
# Implement a breadth first search on the class - which takes an empty array, traverses
# the tree using the Breadth-First Search approach (navingating from left to right), 
# stores all the nodes' names in the input array and then returns it


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array