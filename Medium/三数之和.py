class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lens=len(nums)
        if lens<3:return []
        res=[]
        nums=sorted(nums)
        for i in range(lens-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i + 1, lens - 1
            while left < right:
                if left>i+1 and nums[left]==nums[left-1]:
                    left+=1
                    continue
                if nums[left]+nums[right]+nums[i]==0:
                    res.append([nums[left],nums[right],nums[i]])
                    left+=1
                    right-=1
                elif nums[left]+nums[right]+nums[i]<0:
                    left += 1
                else:
                    right-=1
            i+=1
        return res