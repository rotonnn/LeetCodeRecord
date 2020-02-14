# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        res=[]
        def solu(root):
            if root.left:
                solu(root.left)
            res.append(root.val)
            if root.right:
                solu(root.right)
        solu(root)
        return res