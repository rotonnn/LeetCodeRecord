class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        heights.insert(0,-1)
        lens=len(heights)
        l=[0]*lens
        r=[lens-1]*lens
        for i in range(1,lens-1):
            if heights[i]>heights[i-1]:
                l[i]=i-1
            else:
                tmp=i-1
                while tmp>=0 and heights[tmp]>=heights[i]:
                    tmp=l[tmp]
                l[i]=tmp
        for i in range(lens-2,0,-1):
            if heights[i]>heights[i+1]:
                r[i]=i+1
            else:
                tmp=i+1
                while tmp<=lens-1 and heights[tmp]>=heights[i]:
                    tmp=r[tmp]
                r[i]=tmp
        mx=0
        print(l,r)
        for i in range(1,lens-1):
            mx=max(mx,(r[i]-l[i]-1)*heights[i])
        return mx
        
                