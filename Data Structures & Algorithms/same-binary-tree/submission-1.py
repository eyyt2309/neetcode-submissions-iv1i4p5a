# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = deque()
        q_stack = deque()

        p_stack.append(p)
        q_stack.append(q)

        while p_stack and q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            if p_node and q_node:
                if p_node.val != q_node.val:
                    return False
            elif p_node and not q_node:
                return False
            elif not p_node and q_node:
                return False
            if p_node:
                p_stack.append(p_node.left)
                p_stack.append(p_node.right)
            if q_node:
                q_stack.append(q_node.left)
                q_stack.append(q_node.right)
        
        return True