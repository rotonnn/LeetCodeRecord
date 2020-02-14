class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a,b=nums[0],nums[-1]
        nums.insert(0,a-1)
        nums.append(b-1)
        for i in range(len(nums)):
            if nums[i]<nums[i+1]:
                continue
            return i-1
        
