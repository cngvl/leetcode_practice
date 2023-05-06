require 'pry-byebug'

# @param {Integer[]} flowerbed
# @param {Integer} n
# @return {Boolean}

# Maybe create some sort of stack like the valid paranthesis question?

# Might be able to do some slick things like replacing 000 for 010 n times
  # This doesn't consider the very start / end of the string though
  # Start of string can be 000 > 100
  # End of string can be 000 > 001

# Can do a check at the end to see if there are adjacent 1s

# 00000 > 10101

def can_place_flowers(flowerbed, n)
  start_regex = /^0[^1]/
  end_regex = /00$/
  middle_regex = /000/
  additional_regex = /^0\b/
  no_of_changes = 0
  flowerbed_string = flowerbed.join
  n.times do

    # binding.pry
    if flowerbed_string.match?(start_regex)
      flowerbed_string.gsub!(start_regex, '10')
      no_of_changes += 1
    end

    if flowerbed_string.match?(additional_regex)
      flowerbed_string.gsub!(additional_regex, '1')
      no_of_changes += 1
    end

    if flowerbed_string.match?(end_regex)
      flowerbed_string.gsub!(end_regex, '01')
      no_of_changes += 1
    end

    if flowerbed_string.match?(middle_regex)
      flowerbed_string.sub!(middle_regex, '010')
      no_of_changes += 1
    end

    # binding.pry
    return true if no_of_changes >= n

  end

  # binding.pry
  # return true if flowerbed_string.match?(/^0$/)
  return true if !flowerbed_string.match?('11') && n <= no_of_changes
  return false if n > no_of_changes
  return false

end


flowerbed = [1,0,0,0,1]
n = 1
# >>> true
p "true"
p can_place_flowers(flowerbed, n)

flowerbed = [1,0,0,0,1]
n = 2
# >>> false
p "false"
p can_place_flowers(flowerbed, n)

flowerbed = [1,0,1,0,1,0,1]
n = 0
# >>> true
p "true"
p can_place_flowers(flowerbed, n)

flowerbed = [0,0,1,0,1]
n = 1
# >>> true
p "true"
p can_place_flowers(flowerbed, n)

flowerbed = [1,0,0,0,0,0,0,0,1]
n = 3
# >>> true
p "true"
p can_place_flowers(flowerbed, n)

flowerbed = [0]
n = 1
# >>> true
p "true"
p can_place_flowers(flowerbed, n)

flowerbed = [0,1,0]
n = 1
# >>> false
p "false"
p can_place_flowers(flowerbed, n)

flowerbed = [0,0]
n = 2
# >>> false
p "false"
p can_place_flowers(flowerbed, n)
