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

# Optimized solution based off discussion post from user yongzx
def backspaceCompare2(s, t):
  si, ti = len(s) - 1, len(t) - 1
  s_count = t_count = 0

  while si >= 0 or ti >= 0:
    # stops at non-deleted char in s or -1
    while si >= 0:
      if s[si] == '#':
        s_count += 1
        si -= 1
      elif s_count > 0:
        s_count -= 1
        si -= 1
      else:
        break
    
    # stops at non-deleted char in t or -1
    while ti >= 0:
      if t[ti] == '#':
        t_count += 1
        ti -= 1
      elif t_count > 0:
        t_count -= 1
        ti -= 1
      else: 
        break

    if (ti < 0 <= si) or (si < 0 <= ti):
      return False
    if (ti >= 0 and si >= 0) and s[si] != t[ti]:
      return False

    si -= 1
    ti -= 1
  
  return True





s = 'abb#c'
t = 'abd#c'
# s = "a#c"
# t = "b"

print(backspaceCompare2(s, t))