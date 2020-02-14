class Solution:
    def climbStairs(self, n: int) -> int:
        odd,plu=1,2
        if n==1:return 1
        if n==2:return 2
        for i in range(n-2):
            odd,plu=plu,plu+odd
        return plu