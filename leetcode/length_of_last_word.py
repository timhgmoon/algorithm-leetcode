#58
def lengthOfLastWord(s):
  str_list = s.split()
  last_index = len(str_list) - 1
  
  return len(str_list[last_index])

# s = "   fly me   to   the moon  "
# s = "Hello World"
s = "luffy is still joyboy"
print(lengthOfLastWord(s))

