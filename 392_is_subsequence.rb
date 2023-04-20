# @param {String} s
# @param {String} t
# @return {Boolean}

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Input: s = "axc", t = "ahbgdc"
# Output: false

# def is_subsequence(s, t)
#   test_sub = []
#   t.chars.each do |char|
#     test_sub << char if s.include?(char)
#   end
#   test_sub.join.include?(s)
#   test_sub.join == s
# end


def is_subsequence(s, t)
  point1 = 0
  point2 = 0

  t.chars.each do
    if s[point1] == t[point2]
      point1 += 1
    end
    point2 += 1
  end
  point1 == s.length
end

s = "ab"
t = "baab"

p is_subsequence(s, t)
