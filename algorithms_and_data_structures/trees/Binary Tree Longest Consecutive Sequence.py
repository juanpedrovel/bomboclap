# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        if not root:
            return 0
        max_lenght = 1
        self.stack = []
        current = root
        self.stack.append(current)
        max_lenght = 0
        while self.stack:
            lenght = 1
            lenght_left = 0
            lenght_right = 0
            current = self.stack.pop()
            if current.left:
                if current.left.val == current.val + 1:
                    lenght_left = self.longest(current.left)
                else:
                    self.stack.append(current.left)
            if current.right:
                if current.right.val == current.val + 1:
                    lenght_right = self.longest(current.right)
                else:
                    self.stack.append(current.right)
            lenght += max(lenght_left, lenght_right)
            max_lenght = max(lenght, max_lenght)
        return max_lenght
    
    def longest(self, node):
        lenght = 1
        left_lenght = 0
        right_lenght = 0
        if node.left:
            if node.left.val == node.val + 1:
                left_lenght = self.longest(node.left)
            else:
                self.stack.append(node.left)
        if node.right:
            if node.right.val == node.val + 1:
                right_lenght = self.longest(node.right)
            else:
                self.stack.append(node.right)
        lenght += max(right_lenght, left_lenght)
        return lenght

s = "aaabbcc"
dict = ["aaa","aab","bc"]
d = Solution()
print(d.addBoldTag(s, dict))