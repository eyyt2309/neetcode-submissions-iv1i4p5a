from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        highest = 0

        stack = deque()
        stack.append((root, 1))

        while stack:
            curr = stack.pop()
            if curr[0] is not None:
                highest = curr[1] if curr[1] > highest else highest

                stack.append((curr[0].left, curr[1] + 1))
                stack.append((curr[0].right, curr[1] + 1))

        return highest
        