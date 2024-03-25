# Constraints:
    # 1 <= nums1.length <= nums2.length <= 1000
    # 0 <= nums1[i], nums2[i] <= 104
    # All integers in nums1 and nums2 are unique.
    # All the integers of nums1 also appear in nums2.

# Follow up: Could you find an O(nums1.length + nums2.length) solution?

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        returnArray = []
        for num1Val in nums1:
            # print(f'{num1Index}: {num1Val}')
            appendCheck = False
            for num2Index, num2Val in enumerate(nums2):
                ifCheck = (num2Val > num1Val and num2Index > nums2.index(num1Val)) and appendCheck == False
                if ifCheck:
                    # print(num2Val)
                    returnArray.append(num2Val)
                    appendCheck = True

            if appendCheck == False:
                # print('-1')
                returnArray.append(-1)

        print(returnArray)

sol = Solution()

nums1 = [4,1,2]
nums2 = [1,3,4,2]
# >>> [-1,3,-1]
sol.nextGreaterElement(nums1, nums2)

nums1 = [2,4]
nums2 = [1,2,3,4]
# # >>> [3,-1]
sol.nextGreaterElement(nums1, nums2)
