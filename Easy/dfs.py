# Depth First Search
# You are given a Node class that has a name and array of optional children Nodes
# When put together, Nodes form a tree-like structure. Implement DFS method on the class
# which takes in an empty array, traverses the tree using DFS approach (navigate the 
# tree from left to right), stores all the Nodes' names int he input array and
# returns it


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array 

# v = vertex
# e = edge
# O(v + e) = time complexity
# O(v) = space complexity