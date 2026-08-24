# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                s.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                s.append("None")

        return ",".join(s)
            

    def deserialize(self, data: str) -> Optional[TreeNode]:
        s = data.split(",")

        if s[0] == "None":
            return None

        root = TreeNode(int(s[0]))
        queue = deque([root])

        i = 1

        while queue:
            node = queue.popleft()

            # left child
            if s[i] != "None":
                node.left = TreeNode(int(s[i]))
                queue.append(node.left)
            i += 1

            # right child
            if s[i] != "None":
                node.right = TreeNode(int(s[i]))
                queue.append(node.right)
            i += 1

        return root
