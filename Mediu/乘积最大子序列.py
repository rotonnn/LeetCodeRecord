class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        cur_max=cur_min=res=nums[0]
        for i in nums[1:]:
            if i==0:
                cur_max=cur_min=0
            else:
                tmp=cur_max
                cur_max=max(cur_max*i,cur_min*i,i)
                cur_min=min(tmp*i,cur_min*i,i)
            res=max(res,cur_max,cur_min)
        return res
