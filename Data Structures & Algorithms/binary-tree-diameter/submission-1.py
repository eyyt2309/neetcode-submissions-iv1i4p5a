# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if node == None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if self.diameter < left + right:
                self.diameter = left + right

            height = max(left, right) + 1

            return height

        dfs(root)
        return self.diameter