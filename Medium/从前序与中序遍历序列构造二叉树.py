# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self,preorder,inorder,root):
        if preorder:
            ind=inorder.index(root.val)
            if preorder[0] in inorder[:ind]:
                new=TreeNode(preorder[0])
                root.left=new
                preorder.pop(0)
                self.find(preorder,inorder[:ind],new)
            if ind+1<len(inorder) and preorder[0] in inorder[ind+1:]:
                new=TreeNode(preorder[0])
                root.right=new 
                preorder.pop(0)
                self.find(preorder,inorder[ind+1:],new)
        return 

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root=None
        if preorder:
            root=TreeNode(preorder[0])
            preorder.pop(0)
            self.find(preorder,inorder,root)
        return root
            