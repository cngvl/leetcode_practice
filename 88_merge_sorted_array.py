# import numpy as np

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """

# def merge(nums1, m, nums2, n):
#     # while n > 0:
#         # nums1.replace(0, nums2[0])
#         # [nums2[0] if x == 0 else x for x in nums1]
#         del nums1[m:]
#         nums1.extend(nums2)
#         nums1.sort()
#         # n -= 1
#     # print(nums1[m:])
#     # print(numpy.array_split(nums1,2))
#     # (list(filter((0).__ne__, nums1)) + nums2).sort()
#     # print(nums1 )

def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# >>> [1,2,2,3,5,6]

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# >>> [1]

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# >>> [1]

merge(nums1, m, nums2, n)
