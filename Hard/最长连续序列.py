class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import defaultdict
        mlen,ind=0,0
        if not nums:return 0
        dic=defaultdict(int)
        for i in nums:
            if dic[i]:continue
            dic[i]+=1
            s=dic[i]+dic[i-1]+dic[i+1]
            dic[i]=dic[i-dic[i-1]]=dic[i+dic[i+1]]=s
      
            mlen=max(mlen,s)
        #print(dic)
        return mlen