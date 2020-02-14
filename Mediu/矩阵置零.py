class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col,rank=len(matrix),len(matrix[0])
        h,l=set(),set()
        for i in range(col):
            for j in range(rank):
                if matrix[i][j]:continue
                h.add(i)
                l.add(j)
        h,l=list(h),list(l)
        for i in h:
            matrix[i]=[0]*rank
        for i in l:
            for j in range(col):
                matrix[j][i]=0
        return matrix