class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        while matrix:
            res+=matrix[0]
            matrix.pop(0)
            if matrix:
                for i in matrix:
                    res+=[i[-1]]
                    i.pop()
            while [] in matrix:
                matrix.remove([])
                    
            if matrix:
                res+=matrix[-1][::-1]
                matrix.pop()
            if matrix:
                for i in matrix[::-1]:
                    res+=[i[0]]
                    i.pop(0)
            while [] in matrix:
                matrix.remove([])
        return res
