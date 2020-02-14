class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        if prices:
            cur=prices[0]
            for i in prices:
                if i>cur:
                    res+=i-cur
                    cur=i
                else:
                    cur=i
        return res