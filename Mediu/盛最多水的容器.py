class Solution:
    def maxArea(self, height: list) -> int:
        left, right = 0, len(height) - 1
        res,mx=0,0
        while left != right:
            res = (right - left) * min(height[left], height[right])
            mx=max(mx,res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mx
        