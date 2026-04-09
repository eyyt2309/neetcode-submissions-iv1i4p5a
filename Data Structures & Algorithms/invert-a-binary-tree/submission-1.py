# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque()

        stack.append(root)

        while stack:
            node = stack.pop()
            if node is not None:
                left = node.left
                right = node.right

                temp = right

                node.right = node.left
                node.left = temp
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)

        return root
