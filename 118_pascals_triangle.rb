require 'pry-byebug'

# @param {Integer} num_rows
# @return {Integer[][]}

def generate(num_rows)
  return [[1]] if num_rows == 1
  return [[1], [1, 1]] if num_rows == 2

  big_array = [[1], [1, 1]]
  while num_rows >= 3
    last_array = big_array[-1]
    first_pointer = 0
    next_array = []
    while first_pointer <= last_array.length - 2
      next_array << last_array[first_pointer] + last_array[first_pointer + 1]
      first_pointer += 1
    end

    next_array.unshift(1)
    next_array.push(1)
    big_array << next_array
    num_rows -= 1
  end
  big_array
end

# Very poor attempt at a recursive function
# def generate(num_rows)
#   big_array = []
#   if num_rows == 1
#     return big_array << [1]
#   else
#     small_array = []
#     generate(num_rows - 1)
#   end
# end

# LeetCode Solution
# def generate(num_rows)
#   @memo = {}

#   (1..num_rows).map do |num|
#     recurse(num)
#   end
# end

# def recurse(num)
#   return [1] if num == 1
#   return [1,1] if num == 2

#   result = []

#   return @memo[num-1] if @memo[num-1]

#   recurse(num - 1).each_with_index do |x, index|
#     # byebug
#     binding.pry
#     if index == 0
#       result << x
#     end

#     if index == recurse(num - 1).length - 1
#       result << x
#     end

#     if index < recurse(num - 1).length - 1
#       result << (x + recurse(num - 1)[index + 1])
#     end
#   end

#   @memo[num-1] = result
#   @memo[num-1]
# end

# numRows = 5
# >>> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# numRows = 1
# >>> [[1]]

num_rows = 5
p generate(num_rows)
