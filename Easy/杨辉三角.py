
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i,lst,res=1,[1],[]
        for i in range(numRows):
            res.append(lst)
            yield res[-1]
            a=lst[0]
            lst=[lst[j]+lst[j-1] for j in range(1,len(lst))]
            lst.insert(0,a)
            lst.append(a)
        