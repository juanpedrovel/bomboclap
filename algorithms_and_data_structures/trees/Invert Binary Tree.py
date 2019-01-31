# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invertTree_helper(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            invertTree_helper(root.right)
            invertTree_helper(root.left)
        invertTree_helper(root)
        return root

s = "aaabbcc"
dict = ["aaa","aab","bc"]
d = Solution()
print(d.addBoldTag(s, dict))