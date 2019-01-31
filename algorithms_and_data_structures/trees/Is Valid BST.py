# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        self.last = float('-inf')
        
        def in_order(root):
            if not root:
                return True
            if not in_order(root.left):
                return False
            if root.val > self.last:
                self.last = root.val
            else:
                return False
            if not in_order(root.right):
                return False
            return True
    
        return in_order(root)

time = [[1,0]]
k = 2
d = Solution()
print(d.canFinish(k, time))