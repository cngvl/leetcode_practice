# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
  unique_nums = nums.uniq
  nums.length != unique_nums.length
end

# nums = [1, 2, 3, 1]
nums = [1, 2, 3, 4]
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

p contains_duplicate(nums)
