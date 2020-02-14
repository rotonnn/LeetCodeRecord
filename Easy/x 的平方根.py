class Solution:
    def erfen(self,left,right,x):
        if left+1==right and left*left<x<right*right:
            return left
        if left==right:
            return left
        mid=(left+right)//2
        if mid*mid<x:
            return self.erfen(mid,right,x)
        elif mid*mid>x:
            return self.erfen(left,mid,x)
        else:
            return mid
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        res=self.erfen(0,x,x)
        return res
        