# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def traverse(preorder, inorder):
            if not preorder:
                return None

            node = TreeNode(preorder[0])
            pivot = inorder.index(preorder[0])
            node.left = traverse(preorder[1:pivot+1], inorder[:pivot])
            node.right = traverse(preorder[pivot + 1:], inorder[pivot + 1:])
            return node

        return traverse(preorder, inorder)