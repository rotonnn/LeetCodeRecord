class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lens=len(nums)
        if lens<1:return True
        lst,i=[False]*lens,0
        lst[0],cur_max=True,0
        while lst[i]==True:
            tmp=min(lens-1,i+nums[i])
        
            if tmp==lens-1:return True
            if tmp<=cur_max:
                i+=1
                continue
            cur_max=tmp
            lst[i+1:tmp+1]=[True]*(tmp-i)
 
        
        return False