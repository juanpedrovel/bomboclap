# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

in_order = []
pre_order = []
post_order = []

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    self.inOrder(0)

  def inOrder(self, n):    
    pre_order.append(self.key[n])
    if self.left[n] != -1:
        self.inOrder(self.left[n])
    in_order.append(self.key[n])
    if self.right[n] != -1:
        self.inOrder(self.right[n])
    post_order.append(self.key[n])
                
    return 0

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in in_order))
	print(" ".join(str(x) for x in pre_order))
	print(" ".join(str(x) for x in post_order))

threading.Thread(target=main).start()
