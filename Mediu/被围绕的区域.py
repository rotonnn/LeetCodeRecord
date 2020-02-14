class Solution:
    def dfs(self,board,i,j,vis,flag):
        if vis[i][j]:
            board[i][j]=flag
            vis[i][j]=False
            if i+1<len(board) and vis[i+1][j] and board[i+1][j]!='X':
                self.dfs(board,i+1,j,vis,flag)
            if i-1>=0 and vis[i-1][j] and board[i-1][j]!='X':
                self.dfs(board,i-1,j,vis,flag)
            if j+1<len(board[0]) and vis[i][j+1] and board[i][j+1]!='X':
                self.dfs(board,i,j+1,vis,flag)
            if j-1>=0 and vis[i][j-1] and board[i][j-1]!='X':
                self.dfs(board,i,j-1,vis,flag)
        return 
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0])<3 or len(board)<3:
            return
        vis=[[True] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            if board[i][0]=='O' and vis[i][0]:
                self.dfs(board,i,0,vis,'P')
            if board[i][-1]=='O' and vis[i][-1]:
                self.dfs(board,i,len(board[0])-1,vis,'P')
        
        for j in range(len(board[0])):
            if board[0][j]=='O' and vis[0][j]:
                self.dfs(board,0,j,vis,'P')
            if board[-1][j]=='O' and vis[len(board)-1][j]:
                self.dfs(board,len(board)-1,j,vis,'P')
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='P':
                    board[i][j]='O'
        
