class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        dic=Counter(nums)
        for k in dic:
            if dic[k]==1:return k