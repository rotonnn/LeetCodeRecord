class Solution:
    def ksort(self,nums,left,right):
        
        if left>=right:
            return 
        l,r=left,right
        key=nums[left]
        while l<r:
            while r>l and nums[r]>=key:
                r-=1
            while r>l and nums[l]<=key:
                l+=1
            nums[r],nums[l]=nums[l],nums[r]
        nums[left],nums[l]=nums[l],nums[left]
        self.ksort(nums,left,l-1)
        self.ksort(nums,l+1,right)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums=self.ksort(nums,0,len(nums)-1)