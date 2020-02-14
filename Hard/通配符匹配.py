class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens,lenp=len(s),len(p)
        lst=[[False for i in range(lenp+1)] for j in range(lens+1)]
        lst[0][0]=True
        for i in range(1,lenp+1):
            lst[0][i]=lst[0][i-1] and p[i-1]=='*'

        for i in range(1,lens+1):
            for j in range(1,lenp+1):
                if p[j-1]=='*':
                    lst[i][j]=lst[i-1][j] or lst[i][j-1]
                else:
                    lst[i][j]=lst[i-1][j-1] and (p[j-1]==s[i-1] or p[j-1]=='?')
        #print(lst)
        return lst[-1][-1]