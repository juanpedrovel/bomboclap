class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        lens = len(nums)
        half = lens // 2
        root = TreeNode(nums[half])
        root.left = self.sortedArrayToBST(nums[:half])
        root.right = self.sortedArrayToBST(nums[half+1:])
        return root        

s = [-10,-3,0,5,9]
d = Solution()
x = d.sortedArrayToBST(s)
print(x)