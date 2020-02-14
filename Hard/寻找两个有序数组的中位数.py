class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=sorted(nums1+nums2)
        mid=len(res)//2
        if len(res)%2:
            return res[mid]
        else:
            return (res[mid-1]+res[mid])/2
        