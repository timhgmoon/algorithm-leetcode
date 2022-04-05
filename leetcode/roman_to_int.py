#13

def romanToInt(s):
  roman_dict = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
  }
  
  subtract = 0
  total = 0
  
  for i in range(len(s) - 1):
      if roman_dict[s[i]] < roman_dict[s[i+1]]:
          subtract += roman_dict[s[i]]
      else:
          total += roman_dict[s[i]]
  
  total += roman_dict[s[-1]]
  return total - subtract

# s = "III" #3
# s = "LVIII" #58
s = "MCMXCIV" #1994

print(romanToInt(s))
