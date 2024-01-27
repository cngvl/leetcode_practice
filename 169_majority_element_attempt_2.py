# Constraints:
    # n == nums.length
    # 1 <= n <= 5 * 104
    # -109 <= nums[i] <= 109


# Initialize an element m and a counter c with c = 0
# For each element x of the input sequence:
# If c = 0, then assign m = x and c = 1
# else if m = x, then assign c = c + 1
# else assign c = c − 1
# Return m

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        currentNum = 0
        counter = 0
        for num in nums:
            ifCheck = (counter == 0)
            elifCheck = (currentNum == num)
            if counter == 0:
                currentNum = num
                counter = 1
            elif currentNum == num:
                counter += 1
            else:
                counter -= 1

        # print(currentNum)
        return currentNum





nums = [3,2,3]
# >>> 3

# nums = [2,2,1,1,1,2,2]
# >>> 2

sol = Solution()
sol.majorityElement(nums)
