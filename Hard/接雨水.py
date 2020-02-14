class Solution:
    def rsum(self,height,top,mid):
     
        if not height:return 0
        rtop=max(height)
        ind=height.index(rtop)
    
        sm=self.rsum(height[ind+1:],rtop,ind)
        return min(rtop,top)*ind-sum(height[:ind])+sm
    
    def lsum(self,height,top,mid):
        if not height:return 0
        ltop=max(height)
        ind =height.index(ltop)
        sm=self.lsum(height[:ind],ltop,ind)
        return min(ltop,top)*(len(height)-ind-1)-sum(height[ind+1:mid])+sm

    def trap(self, height: List[int]) -> int:
        if not height:return 0
        num,top,lens=0,max(height),len(height)
        mid=height.index(top)

        num+=self.lsum(height[:mid],top,mid)

        num+=self.rsum(height[mid+1:],top,mid)


        return num
