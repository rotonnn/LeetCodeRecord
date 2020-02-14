class Solution:
    def reverse(self, x: int) -> int:
        symbol=1
        if x<0:
            symbol=-1
            x*=symbol
        lst=list(str(x))
        lst=lst[::-1]
        s=''.join(lst)
        if symbol == -1:
            s = '-' + s
        s=int(s)
        if s > 2 ** 31 - 1 or s < -2 ** 31:
            return 0
        else:
            return s
        
        