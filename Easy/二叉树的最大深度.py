# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def maxDepth(self, root: TreeNode,deep=1) -> int:
        dl,dr=0,0
        if not root:
            return 0
        if root.left:
            dl=self.maxDepth(root.left,deep+1)
        if root.right:
            dr=self.maxDepth(root.right,deep+1)
        
        return max(dl,dr,deep)
    