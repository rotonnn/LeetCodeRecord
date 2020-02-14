class Solution:
    def find(self,prices,mx):
        if not prices or len(prices)==1:
            return mx
        cur=min(prices)
        cur_ind=prices.index(cur)
        if cur_ind+1<len(prices):
            tmp=max(prices[cur_ind+1:])
            mx=max(mx,tmp-cur)
        mx=self.find(prices[:cur_ind],mx)
        return mx
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        if prices:
            res=self.find(prices,0)
        return res