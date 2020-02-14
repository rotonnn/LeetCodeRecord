class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens=len(nums)
        cur1=nums[:lens-k]
        del nums[:lens-k]
        nums.extend(cur1)