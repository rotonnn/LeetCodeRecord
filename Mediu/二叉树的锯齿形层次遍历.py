# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def pre(self,root,res,step):
        res[step].append(root.val)
        if root.left:
            self.pre(root.left,res,step+1)
        if root.right:
            self.pre(root.right,res,step+1)
        return 
        
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        res=defaultdict(list)
        if root:
            self.pre(root,res,0)
        for i in range(len(res)):
            if i%2:
                res[i]=res[i][::-1]
        return res.values()