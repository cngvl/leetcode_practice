require 'pry-byebug'

# @param {Integer} num_rows
# @return {Integer[][]}

# def generate(num_rows)
#   big_array = []
#   while num_rows >= 1
#     small_array = []


#     big_array << small_array
#     num_rows -= 1
#   end
#   p big_array
# end


# def generate(num_rows)
#   big_array = []
#   if num_rows == 1
#     return big_array << [1]
#   else
#     small_array = []
#     generate(num_rows - 1)
#   end
# end

def generate(num_rows)
  @memo = {}

  (1..num_rows).map do |num|
    recurse(num)
  end
end

def recurse(num)
  return [1] if num == 1
  return [1,1] if num == 2

  result = []

  return @memo[num-1] if @memo[num-1]

  recurse(num - 1).each_with_index do |x, index|
    # byebug
    binding.pry
    if index == 0
      result << x
    end

    if index == recurse(num - 1).length - 1
      result << x
    end

    if index < recurse(num - 1).length - 1
      result << (x + recurse(num - 1)[index+1])
    end
  end

  @memo[num-1] = result
  @memo[num-1]
end

numRows = 5
# >>> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# numRows = 1
# >>> [[1]]

p generate(numRows)
