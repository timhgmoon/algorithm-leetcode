def groupAnagrams(strs):
  ans = {}

  for str in strs:
    temp = ''.join(sorted(str))
    if temp in ans:
      ans.get(temp).append(str)
    else:
      ans[temp] = [str]
  
  return ans.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

