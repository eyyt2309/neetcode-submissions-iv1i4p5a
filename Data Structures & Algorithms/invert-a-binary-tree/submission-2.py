# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node == None:
                return

            dfs(node.left)
            dfs(node.right)

            temp = node.left
            node.left = node.right
            node.right = temp

            return

        dfs(root)
        return root