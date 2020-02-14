class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for i in nums:
            tmp=[]
            for j in res:
                tmp.append(j+[i])
            res+=tmp
        return res