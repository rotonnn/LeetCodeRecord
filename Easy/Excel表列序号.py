class Solution:
    def titleToNumber(self, s: str) -> int:
        lens=len(s)-1
        value=0
        for ch in s:
            if lens>0:
                value+=(ord(ch)-ord('A')+1)*(26**lens)
            else:
                value+=ord(ch)-ord('A')+1
            lens-=1
        return value