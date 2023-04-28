require 'pry-byebug'

# @param {String[]} strs
# @return {String[][]}

# First solution was dogshit
def group_anagrams(strs)
  big_stack = []

  strs.each do |str|
    puts str
    if big_stack.join.split('').sort.include?(str.split('').sort.join)
      puts "This is old"

    else
      puts "This is new"
      small_stack = []
      small_stack << str
    end
    # big_stack << small_stack
    # byebug
  end
  # p big_stack
end

# Solution using answers + inbuilt method
# def group_anagrams(strs)
#   strs.sort.group_by { |s| s.chars.sort }.values
# end


strs = ["eat","tea","tan","ate","nat","bat"]
# >>> [["bat"],["nat","tan"],["ate","eat","tea"]]
# strs = ["eat","tea","ate"]

# strs = [""]
# >>> [[""]]

# strs = ["a"]
# >>> [["a"]]


# a = [ ["abc"], ["def"], ["ghi"] ]
# a = [ ["abc"], ["def", "fed"], ["ghi"] ]

group_anagrams(strs)
