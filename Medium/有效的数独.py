from collections import defaultdict
class Solution:
   
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rank=[{} for i in range(9)]
        col=[{} for i in range(9)]
        box=[{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':continue
                ch=board[i][j]

                col[i][ch]=col[i].get(ch,0)+1
                rank[j][ch]=rank[j].get(ch,0)+1
                ind=(i//3)*3+j//3
                box[ind][ch]=box[ind].get(ch,0)+1
                if col[i][ch]>1 or rank[j][ch]>1 or box[ind][ch]>1:return False
        return True