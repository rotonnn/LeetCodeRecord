class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.insert(0,-1)
        lens=len(nums)
        if lens==1:return 0
        if lens==2 : return nums[1]
        for i in range(2,lens) :
            nums[i]=max(nums[i-1],nums[i]+nums[i-2],nums[i])
        return max(nums)