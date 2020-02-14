class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==0 or n==0:return 0
        lst=[[0]*(m+1) for _ in range(n+1)]
        lst[0][1]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                lst[i][j]=lst[i-1][j]+lst[i][j-1]
        print(lst)
        return lst[-1][-1]
