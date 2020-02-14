class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[[None],['()']]
        if n<1:
            return None
        if n==1:
            return res[1]
        for i in range(2,n+1):
            l_cu=[]
            for j in range(i):
                left=res[j]
                right=res[i-1-j]
                for v1 in left:
                    for v2 in right:
                        if v1==None:
                            v1=''
                        if v2==None:
                            v2=''
                        current="(" + v1 + ")" + v2
                        l_cu.append(current)
            res.append(l_cu)
        return res[-1]