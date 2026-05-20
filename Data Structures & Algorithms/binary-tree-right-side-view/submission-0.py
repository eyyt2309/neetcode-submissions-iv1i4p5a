from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        hmap = {}
        stack = deque()
        curr = (root, 0)
        ans = []
        while stack or curr[0] is not None:
            while curr[0] is not None:
                stack.append((curr[0], curr[1]))
                curr = (curr[0].right, curr[1] + 1)
            curr = stack.pop()
            if curr[1] not in hmap and curr[0].val is not None:
                hmap[curr[1]] = curr[0]
            curr = (curr[0].left, curr[1] + 1)
            

        for depth in hmap:
            ans.append((depth, hmap.get(depth, None).val))
        ans.sort()
        return [x[1] for x in ans]