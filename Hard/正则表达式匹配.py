class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens,lenp=len(s)+1,len(p)+1
        res=[[False for _ in range(lens)] for k in range(lenp)]
        res[0][0]=True
        for i in range(1,lenp):
            for j in range(lens):
                if p[i-1]=='*':
                    is_match=j>0 and (p[i-2]==s[j-1] or p[i-2]=='.')
                    res[i][j]=res[i-2][j] or (is_match and res[i][j-1])
                else:
                    is_match =j>0 and (p[i-1]==s[j-1] or p[i-1]=='.')
                    res[i][j]=is_match and res[i-1][j-1]
                    
        return res[-1][-1]