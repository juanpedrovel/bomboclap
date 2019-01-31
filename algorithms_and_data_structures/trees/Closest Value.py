# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        if not root:
            return
        current = root
        candidate = root.val
        while current != None:
            if abs(candidate - target) > abs(current.val - target):
                candidate = current.val
            if target > current.val:
                current = current.right
            elif target < current.val:
                current = current.left
            else:
                return current.val
        return candidate