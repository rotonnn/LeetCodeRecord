class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<2:return nums[0]
        mx,cur=nums[0],nums[0]
        for i in nums[1:]:
            if cur<0:cur=0
            cur+=i
            mx=max(cur,mx)
        return mx
