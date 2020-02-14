class Solution:
    def longestPalindrome(self, s: str) -> str:
        s=s[::-1]
        s = '#' + '#'.join(s) + "#"
        lens=len(s)
        size= [0]*lens
        i, p, po = 0, 0, 0

        for i in range(lens):
            if i > p:
                size[i] = 1
            else:
                size[i] = min(p-i,size[2 * po - i])
            while i + size[i] < lens and i - size[i] >= 0 and s[i + size[i]] == s[i - size[i]]:
                size[i] += 1
            if i + size[i] > p:
                p = i + size[i]
                po = i
        max_len = max(size)
        po=size.index(max_len)
        max_str = s[po - max_len + 1:po + max_len]
    
        return max_str.replace("#",'')