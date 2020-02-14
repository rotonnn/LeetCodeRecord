# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def z(self,root,lst):
        if root.left:
            self.z(root.left,lst)
        lst.append(root.val)
        if root.right:
            self.z(root.right,lst)
        return 
    def isValidBST(self, root: TreeNode) -> bool:
        lst=[]
        if root:
            self.z(root,lst)
        for i in range(1,len(lst)):
            if lst[i]<=lst[i-1]:
                return False
        return True
