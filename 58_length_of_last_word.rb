# @param {String} s
# @return {Integer}
def length_of_last_word(s)
  s.split.last.size
end
# Kinda cheating so I think the intended method / logic behind the question is to use an iteration of the string in reverse order

# Solution using two pointers
# def length_of_last_word(s)
#   word_end_pointer = word_start_pointer = -1

#   while s[word_end_pointer] == ' '
#       word_start_pointer -= 1
#       word_end_pointer -= 1
#   end

#   while s[word_start_pointer - 1] != ' ' && !s[word_start_pointer - 1].nil?
#       word_start_pointer -= 1
#   end

#   word_end_pointer - word_start_pointer + 1
# end

# Solution using two pointers AND recursion
# def length_of_last_word(s, word_start_pointer = -1, word_end_pointer = -1)
#   return length_of_last_word(s, word_start_pointer - 1, word_end_pointer - 1) if s[word_end_pointer] == ' '
#   return length_of_last_word(s, word_start_pointer - 1, word_end_pointer) unless s[word_start_pointer - 1] == ' ' || s[word_start_pointer - 1].nil?

#   word_end_pointer - word_start_pointer + 1
# end
