class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:return 0
        from collections import Counter
        res_dict=Counter(nums)
        res=sorted(res_dict.items(),key=lambda i:i[1],reverse=True)
        return res[0][0]