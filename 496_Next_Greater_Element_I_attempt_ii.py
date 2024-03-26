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
        return returnArray


    # NeetCode solution for brute force method
    def nextGreaterElement2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # O(n * m)
        nums1Idx = { n:i for i,n in enumerate(nums1) }
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            # skips vals that aren't in both lists
            if nums2[i] not in nums1Idx:
                continue
            # (i + 1) means that it will only check the elements downstream of the array
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res

    # NeetCode stack solution
    # Addresses followup Q
    # Space complex of 0(nums1)
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1Idx = { n:i for i,n in enumerate(nums1) }
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]

            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur

            if cur in nums1Idx:
                stack.append(cur)

        return res


sol = Solution()

nums1 = [4,1,2]
nums2 = [1,3,4,2]
# >>> [-1,3,-1]
sol.nextGreaterElement(nums1, nums2)

nums1 = [2,4]
nums2 = [1,2,3,4]
# # >>> [3,-1]
sol.nextGreaterElement(nums1, nums2)
