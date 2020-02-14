class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        tol=[1,1]
        for i in range(1,len(s)):
            sm=0
            if 0<int(s[i])<=9:
                sm+=tol[-1]
            if int(s[i-1:i+1])<=26 and s[i-1]!='0':
                sm+=tol[-2]
            if sm:
                tol.append(sm)
            else:return 0
        return tol[-1]
            