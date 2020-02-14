class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:return 0
        total=0
        while n>=5:
            yu=n%5
            cur=(n-yu)//5
            total+=cur
            n=cur
        return total
                
