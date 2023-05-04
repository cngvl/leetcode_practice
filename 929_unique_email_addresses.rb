require 'pry-byebug'

# @param {String[]} emails
# @return {Integer}


# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# >>> 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

# "alice.z@leetcode.com" and "alicez@leetcode.com" will be sent to the same email address - no need for any transformations?
# DO need transformations if using uniq



def num_unique_emails(emails)
  # Loop through array and 'cleanse' all the strings using if statements?
  # regex to select for the things before the @ - no need for regex, can just use split (ty chatgpt)
    # if no @, remove it
    # 'clean' the selected part
    # can make a new array, or modify the existing array - modifying existing array would be better for memory?
  unique_emails = {}
  emails.each do |email|
    local_name, domain = email.split('@')

    local_name.delete!('.')

    if local_name.include?('+')
      local_name = local_name.split('+')[0]
    end

    # binding.pry

    unique_emails["#{local_name}@#{domain}"] = true
  end

  # p unique_emails
  unique_emails.size

end


# chatGPT solution
# def num_unique_emails(emails)
#   unique_emails = {}
#   emails.each do |email|
#     local, domain = email.split('@')
#     local.delete!('.')
#     local.sub!(/\+.*$/, '')
#     unique_emails["#{local}@#{domain}"] = true
#   end
#   return unique_emails.size
# end


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
p num_unique_emails(emails)
