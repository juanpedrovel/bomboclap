class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        current = root
        if current == None:
            return None
        while current != None:
            if p > current.val:
                current = current.right
            elif p < current.val:
                parent = current
                current = current.left
            else:
                break
        if current == None:
            return None
        if current.right:
            current = current.right
            while current.left != None:
                current = current.left
            return current.val
        else:
            return parent.val

time = TreeNode(2)
time.left = TreeNode(1)
k = 1
d = Solution()
print(d.inorderSuccessor(time, k))