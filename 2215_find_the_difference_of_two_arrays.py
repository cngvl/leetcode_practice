# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        print(nums1, nums2)




nums1 = [1,2,3]
nums2 = [2,4,6]
# Output: [[1,3],[4,6]]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
# Output: [[3],[]]


s = Solution()
s.findDifference(nums1, nums2)
