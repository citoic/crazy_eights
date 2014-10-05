# CS 156 homework 2
# 6 October 2014
# Katharine Brinker and Edward Ciotic

class Node:

    def __init__(self):
        self.parent = None
        self.children = []
        #TODO: insert data that leafs hold
        #TODO: maybe insert a is_leaf field 

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def insert_child(self, child):
        self.children.append(child)

    #TODO: figure out best way to get children


class CrazyEight:

    @staticmethod
    def move(self, partial_state):
        return 0
        
    @staticmethod
    def move_perfect_knowledge(self, state):
        return 0


