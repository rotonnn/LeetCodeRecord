class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lens=len(s)+1
        lst=[False]*lens
        lst[0]=True
        for i in range(1,lens):
           for j in range(i,lens):
               if s[i-1:j] in wordDict and lst[i-1]:
                    lst[j]=True
                    #print(lst)
      
        return lst[-1]