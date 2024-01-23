# Constraints:
    # 1 <= arr.length <= 16
    # 1 <= arr[i].length <= 26
    # arr[i] contains only lowercase English letters.

# First thought is to use a sliding window? - concats must be sequential
# 1 <= arr.length <= 16 - How does this help me?
# Can brute force and check every single combination - is this O(n2)?
    # Can't even do this because it doesn't merge multiple elements together

# "A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements."

# Maybe I try deleting elements rather than trying to merge them?


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        if len(arr) == 1:
            return len(arr[0])

        leftPointer = 0
        rightPointer = 1
        biggestSeen = 0
        while leftPointer < len(arr):
            while rightPointer < len(arr):
                checkWord = arr[leftPointer] + arr[rightPointer]


        return biggestSeen


arr = ["un","iq","ue"]
# >>> 4

# arr = ["cha","r","act","ers"]
# >>> 6

# arr = ["abcdefghijklmnopqrstuvwxyz"]
# >>> 26

sol = Solution()
sol.maxLength(arr)
