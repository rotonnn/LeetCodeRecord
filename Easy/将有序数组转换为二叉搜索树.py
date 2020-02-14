# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def m(self,root,nums):
        if not nums:return 
        mid=nums.index(root.val)
        ml=mid//2
        mr=mid+(len(nums)-mid)//2

        if ml>=0 and ml<mid:
            new=TreeNode(nums[ml])
            root.left=new
            self.m(new,nums[:mid])

        if mr<len(nums) and mr>mid:
            new=TreeNode(nums[mr])
           
            root.right=new
            self.m(new,nums[mid+1:])
        return
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root=None
        if nums:
            mid=len(nums)//2
            root=TreeNode(nums[mid])
            self.m(root,nums)
        return root
