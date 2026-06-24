# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, highest):
            if node == None:
                return 0
            
            if node.val >= highest:
                highest = node.val
                left_good = dfs(node.left, highest)
                right_good = dfs(node.right, highest)
                return 1 + left_good + right_good
            else:
                left_good = dfs(node.left, highest)
                right_good = dfs(node.right, highest)
                return left_good + right_good

        return dfs(root, float('-inf'))    