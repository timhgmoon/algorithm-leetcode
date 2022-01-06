def isAnagram(s, t):
  # s_list = list(s)
  # t_list = list(t)
  # check = False
  # if(len(s) != len(t)):
  #   return check
  # for letter in s_list:
  #   if letter in t_list:
  #     check = True
  #     t_list.remove(letter)
  #   elif (len(t_list) == 0):
  #     return False
  #   else:
  #     return False
  # return check
  #BETTER SOLUTION
  count = {}
  for char in s:
    if char not in count:
      count[char] = 1
    else:
      count[char] += 1

  for char in t:
    if char in count:
      count[char] -= 1
    else:
      return False

  for i in count.values():
    if i != 0:
      return False

  return True

print(isAnagram("anagram", "nagaram"))
