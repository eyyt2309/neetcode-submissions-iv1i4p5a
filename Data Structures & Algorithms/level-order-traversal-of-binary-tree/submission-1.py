from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            length = len(queue)
            level_arr = []
            for i in range(length):
                curr = queue.popleft()
                if curr:
                    level_arr.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level_arr:
                ans.append(level_arr)
            level += 1

        return ans