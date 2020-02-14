class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        s=sorted(strs)
        lens=min(len(s[0]),len(s[-1]))
        res=[]
        for i in range(lens):
            if s[0][i]==s[-1][i]:
                res.append(s[0][i])
            else:
                break
        return ''.join(res)
                