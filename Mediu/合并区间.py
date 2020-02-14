class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals,lens=sorted(intervals),len(intervals)
        if lens<1:return []
        if lens<1:return intervals
        res,i=[],0
        while i<lens:
            mx,j,tmp=intervals[i][1],i+1,[intervals[i][0]]
            while j<lens and intervals[j][0]<=mx:
                mx=max(intervals[j][1],mx)
                j+=1
            i=j
            tmp.append(mx)
            res.append(tmp)
            
        return res
                    