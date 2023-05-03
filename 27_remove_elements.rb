# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}

# nums = [3,2,2,3], val = 3
# 2, nums = [2,2,_,_]
# Your function should return k = 2, with the first two elements of nums being 2.

# nums = [0,1,2,2,3,0,4,2], val = 2
# 5, nums = [0,1,4,0,3,_,_,_]
# Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.

def remove_element(nums, val)
  # can gsub val? / reject
  # remove all vals and then push back in?¿ - seems a bit inefficient
  # return the 'sorted' array or just the number of values left over?
  nums.reject! { |element| element == val}
  nums.length
end
