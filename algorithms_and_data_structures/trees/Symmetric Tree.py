# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [(root, root)]
        while stack:
            left_side, right_side = stack.pop()
            if left_side == None or right_side == None:
                return False
            if left_side.val != right_side.val:
                return False
            if left_side.left or right_side.right:
                stack.append((left_side.left, right_side.right))
            if left_side.right or right_side.left:
                stack.append((left_side.right, right_side.left))
        return True

s = "aaabbcc"
dict = ["aaa","aab","bc"]
d = Solution()
print(d.addBoldTag(s, dict))