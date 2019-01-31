# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        if root == None:
            return 0
        self.max_value = 0
        current = root
        Q = []
        Q.append(current)
        while Q:
            value = 0
            current = Q.pop()
            if current.left != None:
                if current.left.val == current.val:
                    value_temp_left, Q_temp = self.DFS(current.left)
                    value += value_temp_left
                    Q += Q_temp
                else:
                    Q.append(current.left)
                
            if current.right != None:
                if current.right.val == current.val:
                    value_temp_right, Q_temp = self.DFS(current.right)
                    value += value_temp_right
                    Q += Q_temp
                else:
                    Q.append(current.right)
            self.max_value = max(self.max_value, value)
        return self.max_value
                    
                    
    def DFS(self, current):
        value = 1
        value_temp_left = 0
        value_temp_right = 0
        Q = []
        if current.left != None:
            if current.left.val == current.val:
                value_temp_left, Q_left = self.DFS(current.left)
                Q += Q_left
            else:
                Q.append(current.left)
                
        if current.right != None:
            if current.right.val == current.val:
                value_temp_right, Q_right = self.DFS(current.right)
                Q += Q_right
            else:
                Q.append(current.right)

        value += max(value_temp_left, value_temp_right)
        self.max_value = max(self.max_value, value_temp_left + value_temp_right)
  
        return value, Q