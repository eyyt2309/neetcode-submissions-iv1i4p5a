from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = deque()
        stack2 = deque()

        stack1.append(p)
        stack2.append(q)

        while stack1 and stack2:

            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 is not None and node2 is not None and node1.val != node2.val:
                return False
            elif node1 is None and node2 is not None:
                return False
            elif node1 is not None and node2 is None:
                return False

            if node1 is not None:
                stack1.append(node1.left)
                stack1.append(node1.right)
            if node2 is not None:
                stack2.append(node2.left)
                stack2.append(node2.right)

        return True    