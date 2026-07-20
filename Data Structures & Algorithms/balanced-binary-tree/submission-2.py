# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True
            
            left, left_balance = dfs(node.left)
            right, right_balance = dfs(node.right)

            return max(left, right) + 1, left_balance and right_balance and abs(left - right) <= 1

        _, balanced = dfs(root)
        return balanced