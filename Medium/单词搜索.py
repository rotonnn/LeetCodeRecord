class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,i,j,vis,word):
            if not word:
                return True
            a=b=c=d=False
            vis[i][j]=False
            if i+1<len(board) and board[i+1][j]==word[0] and vis[i+1][j]:
                a=dfs(board,i+1,j,vis,word[1:])
                if a :return True
            if i-1>=0 and board[i-1][j]==word[0] and vis[i-1][j]:
                b=dfs(board,i-1,j,vis,word[1:])
                if b:return True
            if j+1<len(board[0]) and board[i][j+1]==word[0] and vis[i][j+1]:
                c=dfs(board,i,j+1,vis,word[1:])
                if c:return True
            if j-1>=0 and board[i][j-1]==word[0] and vis[i][j-1]:
                d=dfs(board,i,j-1,vis,word[1:])
                if d:return True
            vis[i][j]=True
            return False
        col,rank=len(board),len(board[0])
        vis=[[True]*rank for _ in range(col)]
        for i in range(col):
            for j in range(rank):
                if vis[i][j] and board[i][j]==word[0]:
                    vis[i][j]=False
                    if dfs(board,i,j,vis,word[1:]):return True
                    vis[i][j]=True
        return False