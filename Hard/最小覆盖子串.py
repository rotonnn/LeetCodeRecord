class Solution:
    def isvalid(self,tmp,t):
        for i in t.keys():
            if not tmp[i]:return False
            if tmp[i]<t[i]:return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        dic_t=Counter(t)
        l,r,lens=0,0,len(s)
        if lens<1:return ""
        tmp,m_s,m_len = Counter(),'',len(s)
        while r<lens:
            tmp[s[r]]+=1
            while self.isvalid(tmp,dic_t):
                if m_len>=r-l:
                    m_len,m_s=r-l,s[l:r+1]
                tmp[s[l]]-=1
                l+=1
            r+=1
        return m_s