class Solution:
    def ksort(self,nums,left,right):
        if left>=right:
            return 
        l,r,key=left,right,nums[left]
        while l<r:
            while l<r and nums[r]>=key:
                r-=1
            while l<r and nums[l]<=key:
                l+=1
            nums[l],nums[r]=nums[r],nums[l]
        nums[left],nums[l]=nums[l],nums[left]
        self.ksort(nums,left,l-1)
        self.ksort(nums,l+1,right)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            nums1[m]=i
            m+=1
        self.ksort(nums1,0,len(nums1)-1)