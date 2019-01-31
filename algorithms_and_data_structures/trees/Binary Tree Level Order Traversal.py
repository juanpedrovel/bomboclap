# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            temp = []
            tempq = []
            for node in queue:
                temp.append(node.val)
                if node.left:
                    tempq.append(node.left)
                if node.right:
                    tempq.append(node.right)
            result.append(temp)
            queue = tempq
        return result

s = "aaabbcc"
dict = ["aaa","aab","bc"]
d = Solution()
print(d.addBoldTag(s, dict))