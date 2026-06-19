class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            
            return (
                a.val == b.val and
                sameTree(a.left, b.left) and
                sameTree(a.right, b.right)
            )

        def dfs(node):
            if node is None:
                return False
            
            if sameTree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)