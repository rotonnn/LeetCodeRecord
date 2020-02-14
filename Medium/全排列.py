class Solution:
    def rank(self,nums,step,res):
        if step+1==len(nums):
            res.append(nums[:])
            return 
        for i in range(step,len(nums)):
            nums[i],nums[step]=nums[step],nums[i]
            self.rank(nums,step+1,res)
            nums[i],nums[step]=nums[step],nums[i]
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.rank(nums,0,res)
        return res
