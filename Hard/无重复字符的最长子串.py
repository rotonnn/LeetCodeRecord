
class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        mx,lst=0,[]
        for i in s:
            if i in lst:
                ind=lst.index(i)
                lst=lst[ind+1:]
            lst.append(i)
            mx=max(mx,len(lst))
        return mx