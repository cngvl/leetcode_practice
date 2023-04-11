def search(nums, target)
  return -1 if !nums.include?(target)
  # Set low + mid + high?
  low = nums[0]
  high = nums[-1]
    mid = (low + high) / 2
  while target != mid do
    if mid < target
      low = mid
      mid = (low + high) / 2
    elsif mid > target
      high = mid
      mid = (low + high) / 2
    end
  end
  return nums.index(mid)
end


# nums = [-1,0,3,5,9,12]
nums = [2,5]
target = 5

p search(nums, target)
