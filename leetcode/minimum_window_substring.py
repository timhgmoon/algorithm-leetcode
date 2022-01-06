import copy
def minWindow(s, t):
  s_list = []
  t_list = []
  answer_list = []
  new_ans = []
  ans_s = ""
  count = 0
  if s == t:
      return s
  if len(s) == 1 and len(t) == 1 or len(s) == 0 and len(t) == 0:
      return ans_s
  if len(s) < len(t):
      return ans_s
  
  for i in range(len(s)):
      s_list.append(s[i])
  for i in range(len(t)):
      t_list.append(t[i])

  for i in s_list:
      if i in t_list:
          count += 1
      if count > 0:
          answer_list.append(i)
      if all(elem in answer_list for elem in t_list):
          new_ans.append(copy.deepcopy(answer_list))
          answer_list.clear()
          count = 0
  # print(min(new_ans, key = len))
  if len(new_ans) == 0:
      return ans_s
  return ans_s.join(min(new_ans, key=len))


s = "ABC"
t = "CAB"
print(minWindow(s, t))
