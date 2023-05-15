require 'pry-byebug'

# input 's' is a string

# Check through each of the characters in the string sequentually
  # if it is an opening, add it to an array
  # ONLY OPENING BRACKETS ARE STORED IN THE ARRAY
  # if a following char is a matching closing bracket for anything in the array, clear the opening bracket stored in the array
# Finally, check if the array is empty
  # if it's empty then everything checks out
  # else there was an error in the string
# donezo

def is_valid(s)
  stack = []
  s.each_char do |char|
    case char
    when '(' , '[' , '{'
      stack << char
    when ')'
      return false if stack.pop != '('
    when ']'
      return false if stack.pop != '['
    when '}'
      return false if stack.pop != '{'
    end
  end
  stack.empty?
end

# s = '()[]{}'
# p is_valid(s)

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false
