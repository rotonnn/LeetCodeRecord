class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import Counter,defaultdict
        p_num=Counter([tuple(point) for point in points])
        p_elem=list(p_num.keys())
        res=0

        def gcd(x,y):
            if y==0:return x
            else:return gcd(y,x%y)
       
        num=len(p_elem)
        if num==1:return p_num[p_elem[0]]
        if num<1:return 0
        for i in range(num-1):
            x1,y1=p_elem[i][0],p_elem[i][1]
            slope=defaultdict(int)
            
            for j in range(i+1,num):
                x2,y2=p_elem[j][0],p_elem[j][1]
                dx,dy=x2-x1,y2-y1
                mul=gcd(dy,dx)
                if mul!=0:
                    dx//=mul
                    dy//=mul
                slope["{}/{}".format(dx,dy)]+=p_num[p_elem[j]]
            res=max(res,p_num[p_elem[i]]+max(slope.values()))

        return res
            

            
