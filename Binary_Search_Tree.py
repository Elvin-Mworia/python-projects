class Node:
    def __init__(self,data=None):
        self.data=data
        self.left_child=None
        self.right_child=None
class Binary_Search_Tree(Node):
    def __init__(self):
        self.root_node=None

    def min_node(self):
            current=self.root_node
            while current.left_child:
                current=current.left_child
            
            return current