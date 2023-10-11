# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000

# Notes:
    # Initial thought was to just loop through each element in both arrays and then check if its in the other array but then that's an n2 time complex?
    # Alternative is to go through each array and 'convert' it to a hash
    # AND THEN loop through the array / hash to see if its in the opposing hashmap
        # Takes away some memory but significantly cuts down on the time

    # Need to be careful of empty arrays and arrays that are identical
    # Another way would be to create a duplicate of both arrays and then remove any identical values?
        # This is another n2 time complex solution

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        nums1Hash = {}
        nums2Hash = {}

        nums2MissingValues = []
        nums1MissingValues = []

        for num in nums1:
            if num not in nums1Hash:
                nums1Hash[num] = True

        for num in nums2:
            if num not in nums2Hash:
                nums2Hash[num] = True


        for num in nums1Hash:
            if num not in nums2Hash:
                nums2MissingValues.append(num)

        for num in nums2Hash:
            if num not in nums1Hash:
                nums1MissingValues.append(num)



        print([nums2MissingValues, nums1MissingValues])




# nums1 = [1,2,3]
# nums2 = [2,4,6]
# >>> [[1,3],[4,6]]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
# >>> [[3],[]]


s = Solution()
s.findDifference(nums1, nums2)
