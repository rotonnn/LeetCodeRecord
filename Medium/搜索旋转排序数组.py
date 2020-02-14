class Solution:
    def point(self,nums,left,right):
        if left+1==right or left==right:
            return None
        if nums[left]>nums[right-1]:
            mid=(left+right)//2
            l=self.point(nums,left,mid)
            r=self.point(nums,mid,right)
            if not(l or r):return mid
            return r if r else l

    def erfen(self,nums,left,right,target):
        if nums[left]==target:
            return left
        if left+1==right or left==right:return -1
        mid=(left+right)//2
        if nums[mid]>target:
            return self.erfen(nums,left,mid,target)
        else:
            return self.erfen(nums,mid,right,target)
    
    def search(self, nums: List[int], target: int) -> int:
        lens=len(nums)

        if not lens or (lens==1 and nums[0]!=target):return -1
        if lens==1 and nums[0]==target:return 0
        mid=self.point(nums,0,lens)
        if not mid :
            return self.erfen(nums,0,lens,target)
        if nums[0]>target:
            return self.erfen(nums,mid,lens,target)
        else:
            return self.erfen(nums,0,mid,target)