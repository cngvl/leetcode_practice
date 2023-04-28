require 'pry-byebug'

# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
  # Is there a way to loop through all elements at the same time? - Probably don't need to do this
  # Can store letters in a stack?
  smallest_char_count = strs.min_by(&:length).length
  letter_pos = 0
  big_stack = []
  while smallest_char_count > letter_pos
    small_stack = []
    strs.each do |str|
      small_stack << str[letter_pos]
    end
    letter_pos += 1
    big_stack << small_stack if small_stack.uniq.length == 1
    # byebug
  end
  p big_stack.uniq.join('')
end

strs = ["flower","flow","flight"]
# >>> "fl"

# strs = ["dog","racecar","car"]
# >>> ""

longest_common_prefix(strs)
