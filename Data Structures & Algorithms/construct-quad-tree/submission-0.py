"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recurse(arr):
            total = sum(sum(arr, []))
            if total == len(arr) * len(arr[0]):
                return Node(
                    val=True,
                    isLeaf=True
                )
            elif total == 0:
                return Node(
                    val=False,
                    isLeaf=True
                )
            row_mid = len(arr) // 2
            col_mid = len(arr[0]) // 2

            node = Node()
            node.topLeft = recurse([row[:col_mid] for row in arr[:row_mid]])
            node.topRight = recurse([row[col_mid:] for row in arr[:row_mid]])
            node.bottomLeft = recurse([row[:col_mid] for row in arr[row_mid:]])
            node.bottomRight = recurse([row[col_mid:] for row in arr[row_mid:]])

            return node
        return recurse(grid)
            