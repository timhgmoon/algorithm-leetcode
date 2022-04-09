# 739

#Brute force O(n^2) [not good]
def dailyTemperatures(temperatures):
  answer = []
  for i in range(len(temperatures)):
    current = temperatures[i]
    answer.append(0)
    for j in range(i + 1, len(temperatures)):
      if current < temperatures[j]:
        answer[i] = j - i
        break
  return answer

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))