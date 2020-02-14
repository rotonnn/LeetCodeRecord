class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lens,i=len(nums),0
        while i<lens:
            if nums[i]>lens or nums[i]<1 or nums[i]==i+1:
                i+=1
                continue
            tmp=nums[i]
            if nums[i]==nums[tmp-1]:
                i+=1
                continue
            nums[i],nums[tmp-1]=nums[tmp-1],nums[i]

          

        for i in range(lens):
            if i+1!=nums[i]:
                return i+1
        return lens+1