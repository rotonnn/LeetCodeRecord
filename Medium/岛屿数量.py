class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col=len(grid)
  
        if col==0:return 0
        rank=len(grid[0])
        cnt=0
        for i in range( col):
            for j in range(rank):
                if grid[i][j]=='1':
                    def bfs(i,j):
                        grid[i][j]='0'
                        if i+1<col and grid[i+1][j]=='1':
                            bfs(i+1,j)
                        if i-1>=0 and grid[i-1][j]=='1':
                            bfs(i-1,j)
                        if j+1<rank and grid[i][j+1]=='1':
                            bfs(i,j+1)
                        if j-1>=0 and grid[i][j-1]=='1':
                            bfs(i,j-1)
                        return
                    bfs(i,j)
                    cnt+=1
        return cnt