# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, low, high):
            if node == None:
                return 

            if low <= node.val <= high:
                return node
            elif node.val > high:
                return dfs(node.left, low, high)
            elif node.val < low:
                return dfs(node.right, low, high)
        
        if p.val < q.val:
            return dfs(root, p.val, q.val)
        else:
            return dfs(root, q.val, p.val)