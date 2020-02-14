# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def z(self,l,r):
        if not(l or r):
            return True
        
        if l and r and l.val==r.val:
            #print(l.val,r.val)
            return self.z(l.left,r.right) and self.z(l.right,r.left)

        return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.z(root,root)
        return False