# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.highest = float('-inf')

        def dfs(node):
            if node == None:
                return 0, float('-inf')
            
            left_chain, left_path = dfs(node.left)
            right_chain, right_path = dfs(node.right)

            best_chain = node.val + max(0, left_chain, right_chain)

            path_through_node = (
                node.val 
                + max(0, left_chain) 
                + max(0, right_chain)
            )

            best_path = max(
                left_path,
                right_path,
                path_through_node
            )
            
            return best_chain, best_path

        chain, path = dfs(root)
        return path
        
