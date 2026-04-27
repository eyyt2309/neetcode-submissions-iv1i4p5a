# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0

        ans = self.findNodes(root, float('-inf'))

        return ans

    def findNodes(self, node, largest):

        if node is None:
            return 0

        if largest <= node.val:
            largest = node.val
            return 1 + self.findNodes(node.left, largest) + self.findNodes(node.right, largest)

        return self.findNodes(node.left, largest) + self.findNodes(node.right, largest)
        
