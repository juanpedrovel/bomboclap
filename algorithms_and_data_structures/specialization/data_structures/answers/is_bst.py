#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

nodes = int(sys.stdin.readline().strip())
key = [0] * nodes
left = [0] * nodes
right = [0] * nodes
in_order = []

def IsBinarySearchTree(root, nodes):
    if nodes == 0:
        return True
    inOrder(root)
    for i in range(nodes - 1):
        if in_order[i] > in_order[i+1]:
            return False
    return True
    
def inOrder(n):
    if left[n] != -1:
       inOrder(left[n])
    in_order.append(key[n])
    if right[n] != -1:
       inOrder(right[n])
                
    return 0

def main():
  for i in range(nodes):
      [a, b, c] = map(int, sys.stdin.readline().split())
      key[i] = a
      left[i] = b
      right[i] = c
  if IsBinarySearchTree(0, nodes):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
