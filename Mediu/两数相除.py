class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        tag=1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            tag=-1
        
        divisor,dividend=abs(divisor),abs(dividend)
        res=0
        while dividend>=divisor:
            mul,current=1,divisor
            while dividend>=current:
                dividend-=current
                res+=mul
                current+=current
                mul+=mul
            
        return min(max(res*tag,-2**31),2**31-1)