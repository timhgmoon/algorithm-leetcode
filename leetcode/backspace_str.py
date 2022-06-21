# 844. Backspace String Compare

# Time Complexity: O(n) Space Complexity: O(n)
def backspaceCompare(s, t):
  s_len = len(s)
  t_len = len(t)
  s_ans = ''
  t_ans = ''
  
  for i in range(s_len):
    if len(s_ans) == 0 and s[i] == '#':
      continue
    if s[i] != '#':
      s_ans += s[i]
    else:
      s_ans = s_ans[:len(s_ans) -1]
          
  for i in range(t_len):
    if len(t_ans) == 0 and t[i] == '#':
      continue
    if t[i] != '#':
      t_ans += t[i]
    else:
      t_ans = t_ans[:len(t_ans) -1]
  
  return s_ans == t_ans

# s = 'ab#c'
# t = 'ad#c'
s = "a#c"
t = "b"

print(backspaceCompare(s, t))