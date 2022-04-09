
# 739
#Brute force O(n^2) [not good]
# def dailyTemperatures(temperatures):
#   answer = []
#   for i in range(len(temperatures)):
#     current = temperatures[i]
#     answer.append(0)
#     for j in range(i + 1, len(temperatures)):
#       if current < temperatures[j]:
#         answer[i] = j - i
#         break
#   return answer

#taken off discussion page **NOT MY WORK** (using as reference)
#link to original work
#https://leetcode.com/problems/daily-temperatures/discuss/1574808/C%2B%2BPython-3-Simple-Solutions-w-Explanation-Examples-and-Images-or-2-Monotonic-Stack-Approaches
def dailyTemperatures(temperatures):
  ans = [0] * len(temperatures)

  #stack
  s = []

  for current in range(len(temperatures)-1, -1, -1):
    while s and temperatures[s[-1]] <= temperatures[current]:
      s.pop()
    ans[current] = s[-1] - current if s else 0
    s.append(current)
  return ans


temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))