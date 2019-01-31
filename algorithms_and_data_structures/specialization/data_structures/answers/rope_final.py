# python3

import sys

root = None
class Node:
    def __init__(self, l, key, left, right, parent):
        (self.key, self.l, self.left, self.right, self.parent) = (key, l, left, right, parent) 


class Rope:
    def __init__(self, s):
        self.s = list(s)
        for n, l in enumerate(self.s):
            self.insert(n, l)

    def update(self, v):
        if v == None:
            return
        if v.left != None:
            v.left.parent = v
        if v.right != None:
            v.right.parent = v

    def insert(self, key, l):
        global root
        (left, right) = self.split(root, key)
        new_node = None
        if right == None or right.key != x:
          new_node = Node(l, key, None, None, None)  
        root = self.merge(self.merge(left, new_node), right)

    def split(self, root, key):  
        (result, root) = self.find(root, key)  
        if result == None:    
            return (root, None)  
        right = self.splay(result)
        left = right.left
        right.left = None
        if left != None:
            left.parent = None
        self.update(left)
        self.update(right)
        return (left, right)

    def find(self, root, key): 
        v = root
        last = root
        next = None
        while v != None:
            if v.key >= key and (next == None or v.key < next.key):
                next = v    
            last = v
            if v.key == key:
                break    
            if v.key < key:
                v = v.right
            else: 
                v = v.left      
        root = self.splay(last)
        return (next, root)

    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        while right.left != None:
            right = right.left
        right = self.splay(right)
        right.left = left
        self.update(right)
        return right

    def splay(self, v):
        if v == None:
            return None
        while v.parent != None:
            if v.parent.parent == None:
                self.smallRotation(v)
                break
            self.bigRotation(v)
        return v

    def smallRotation(self, v):
        parent = v.parent
        if parent == None:
            return
        grandparent = v.parent.parent
        if parent.left == v:
            m = v.right
            v.right = parent
            parent.left = m
        else:
            m = v.left
            v.left = parent
            parent.right = m
        self.update(parent)
        self.update(v)
        v.parent = grandparent
        if grandparent != None:
            if grandparent.left == parent:
                grandparent.left = v
            else: 
                grandparent.right = v

    def bigRotation(self, v):
        if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        else: 
        # Zig-zag
            self.smallRotation(v)
            self.smallRotation(v)

    def sum(self, fr, to): 
        global root
        (left, middle) = self.split(root, fr)
        (middle, right) = self.split(middle, to + 1)
        ans = middle.sum
        return ans

    def result(self):
        return ''.join(self.s)
    
    def OrderKeys(self, root, change):
        if root == None:
            return
        self.change_keys(root, change)

    def change_keys(self, node, change):
        node.key += change
        self.s[node.key] = node.l
        if node.left != None:
            self.change_keys(node.left, change)
        if node.right != None:
            self.change_keys(node.right, change)
        return

        
    def process(self, i, j, k):
        global root
        (left, middle) = self.split(root, i)
        (middle, right) = self.split(middle, j + 1)
        if k > i:
            (right_left, right_right) = self.split(right, k + j - i + 1)
            self.OrderKeys(middle, k - i)
            self.OrderKeys(right_left, -(j - i + 1))
            root = self.merge(self.merge(left, right_left), self.merge(middle, right_right))
        elif k < i:
            (left_left, left_right) = self.split(left, k)
            self.OrderKeys(middle, k - i)
            self.OrderKeys(left_right, j - i + 1)
            root = self.merge(self.merge(left_left, middle), self.merge(left_right, right))

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
