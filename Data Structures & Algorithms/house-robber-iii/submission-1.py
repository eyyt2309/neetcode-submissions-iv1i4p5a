# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        # if steal, able to steal or not
        def dfs(node, steal):
            if not node:
                return 0

            if (node, steal) in memo:
                return memo[(node, steal)]

            if steal:
                memo[(node, steal)] = max(
                    node.val + dfs(node.left, False) + dfs(node.right, False),
                    dfs(node.left, True) + dfs(node.right, True)
                )
            else:
                memo[(node, steal)] = dfs(node.left, True) + dfs(node.right, True)


            return memo[(node, steal)]

        return max(dfs(root, True), dfs(root, False))
            