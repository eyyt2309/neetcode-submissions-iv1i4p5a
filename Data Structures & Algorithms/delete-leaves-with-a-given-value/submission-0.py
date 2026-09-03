# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return False
            if node.left == None and node.right == None and node.val == target:
                return True

            if dfs(node.left):
                node.left = None
            if dfs(node.right):
                node.right = None

            if node.left == None and node.right == None and node.val == target:
                return True


        if dfs(root):
            return None
        return root