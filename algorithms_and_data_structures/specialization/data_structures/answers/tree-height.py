# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, index):
        self.index = index

        self.childrens = []

    def add_children(self, children):
        self.childrens.append(children)

        
class TreeHeight:
    def __init__(self):
        self.nodes = []
        self.root = None
    
    def allocate_nodes(self):
            for i in range(self.n):
                x = Node(i)
                if self.parents[i] == -1:
                    self.root = x
                self.nodes.append(x)
                
            for i in range(self.n):
                if self.parents[i] != -1:
                    self.nodes[self.parents[i]].add_children(self.nodes[i])
            return


    def read(self):
                input = sys.stdin.read()
                self.n, *self.parents = list(map(int, input.split()))
               
                
    def compute_height(self, Node):
        if not Node.childrens:
            return 1
        else:
            return 1 + max([ self.compute_height(x) for x in Node.childrens ])
                        

#if __name__ == "__main__":
#  tree = TreeHeight()
#  tree.read()
#  tree.allocate_nodes()
#  print(tree.compute_height(tree.root))

def main():
    tree = TreeHeight()
    tree.read()
    tree.allocate_nodes()
    print(tree.compute_height(tree.root))

threading.Thread(target=main).start()



