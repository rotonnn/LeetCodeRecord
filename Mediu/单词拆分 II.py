class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
        lens=len(s)
        min_len=max_len=len(wordDict[0])
        wordDict=set(wordDict)
        for i in wordDict:
            min_len=min(len(i),min_len)
            max_len=max(len(i),max_len)
        
        def find(ind):
            if ind not in res:
                cur=[]
                for i in range(min_len,min(max_len,lens-ind)+1):
                    if s[ind:ind+i] in wordDict:
                        cur.extend(list(map(lambda x:s[ind:ind+i]+' '+x,find(ind+i))))
                res[ind]=cur
            return res[ind]
        res={lens:['']}
        return list(map(lambda x:x[:-1],find(0)))