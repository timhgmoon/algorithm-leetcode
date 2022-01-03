def isValid(s):
  new_l = []
  if(len(s) % 2 != 0 or len(s) == 0):
    return False
  for letter in s:
    # print('test)')
    if(letter == ')' and new_l):
      if(new_l.pop() != '('):
        return False
    elif(letter == '}' and new_l):
      if(new_l.pop() != '{'):
        return False
    elif(letter == ']' and new_l):
      if(new_l.pop() != '['):
        return False
    else:
      new_l.append(letter)
  return not new_l

print(isValid('()'))