# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    mx=None
    def __init__(self):
        self.mx=None
    def maxPathSum(self, root: TreeNode) -> int:
        if root:
            def deep(root):
                
                if not(root.left or root.right):
                
                    if self.mx==None:
                        self.mx=root.val
                    else:
                        self.mx=max(self.mx,root.val)
                    return root.val
                l=r=0
                if root.left:
                    deep(root.left)
                    l=root.left.val
                if root.right:
                    deep(root.right)
                    r=root.right.val
                self.mx=max(self.mx,l+root.val,r+root.val,root.val,l+r+root.val)
                root.val=max(l+root.val,r+root.val,root.val)
                print(self.mx)
                return root.val
            deep(root)
            return self.mx
