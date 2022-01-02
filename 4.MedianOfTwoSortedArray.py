# 说好的Hard呢
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        length = len(num)
        if length % 2 == 1:
            return num[length//2]
        else:
            return (num[int(length/2)] + num[int(length/2) - 1])/2