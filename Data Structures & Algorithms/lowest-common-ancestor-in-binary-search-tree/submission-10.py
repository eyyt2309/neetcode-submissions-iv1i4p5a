# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# p <= LCA <= q

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val >= q.val:
            return self.dfs(root, q.val, p.val)
        else:
            return self.dfs(root, p.val, q.val)
    
    def dfs(self, node, lower, upper):
        if not node:
            return None
        if node.val == lower or node.val == upper:
            return node
        # if reachable from this node, try to go lower in the tree
        left = self.dfs(node.left, lower, upper)
        right = self.dfs(node.right, lower, upper)

        if left and right:
            return node

        return left or right