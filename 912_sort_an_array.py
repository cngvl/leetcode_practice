# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# You must solve the problem without using any built-in functions
# in O(nlog(n)) time complexity and with the smallest space complexity possible.

# One of the biggest issues with this question is the requirement to run in nlog(n) time complex

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M + 1], arr[M + 1:R + 1]
            # left = arr[L:M + 1] because the latter value is NON-INCLUSIVE
            # right = arr[M + 1:R + 1] because the former value is INCLUSIVE
            # latter value for the right array is because we want to include R
            i, j, k = L, 0, 0
            # i is the pointer for the array
            # j is for the left subarray
            # k is for the right subarray


            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            # These while loops will only run AFTER the merging of the array has been done
            # but there will be 'leftover' values which just need to be inserted
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            # This is the base case for the recursive function
            if l == r:
                return arr

            m = (l + r) // 2
            # Calling a recursive function on the LEFT half of the array
            mergeSort(arr, l, m)

            # Calling a recursive function on the RIGHT half of the array
            mergeSort(arr, m + 1, r)

            # Calling a helper function
            merge(arr, l, m, r)

            return arr

        return mergeSort(nums, 0, len(nums) - 1)


nums = [5, 2, 3, 1]
# >>> [1, 2, 3, 5]

nums = [5, 1, 1, 2, 0, 0]
# >>> [0, 0, 1, 1, 2, 5]

s = Solution()
s.sortArray(nums)
