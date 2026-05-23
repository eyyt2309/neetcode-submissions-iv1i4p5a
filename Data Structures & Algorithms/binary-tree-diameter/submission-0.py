# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.highest = 0
        def dfs(node):
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            height = max(left, right) + 1
            diameter = left + right 
            if self.highest < diameter:
                self.highest = diameter
            return height
        
        dfs(root)
        return self.highest

            