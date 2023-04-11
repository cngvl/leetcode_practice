require 'pry-byebug'

# Example solution using hash maps
# def two_sum(nums, target)
#   hash = {}
#    nums.each_with_index do |number, index|
#        if hash[target - number]
#            return [hash[target - number], index]
#        else
#            hash[number] = index
#        end
#    end
# end

# My initial solution
# def two_sum(nums, target)
#   nums.each_with_index do |first_num, first_index|
#     nums.each_with_index do |sec_num, sec_index|
#       if sec_index != first_index && (sec_num + first_num == target)
#         # puts "entering inner loop"
#         # puts "first num = #{first_num} "
#         # puts "first index = #{first_index} "
#         # puts "second number = #{sec_num}"
#         # puts "second index = #{sec_index}"
#         return [first_index, sec_index]
#       end
#     end
#   end
# end

# My new solution using help without the use of hash maps (probably easiest to use hash)

def two_sum(nums, target)
  nums.each_with_index do |num, index|
    return [index, nums.find_index(target - num)] if nums.slice(0, index).include? target - num
  end
end

# array = [2,7,4,5]
# array = [3,3]
# array = [0,4,3,0]
# array = [-1,-2,-3,-4,-5]
array = (1..10000).to_a

# p two_sum(array, 12)
# p two_sum(array, -8)
p two_sum(array, 19999)
