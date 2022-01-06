def merge(intervals):
  if len(intervals) < 2:
      return [intervals[0]]
  intervals.sort()
  ans = [intervals[0]]
  for i in range(len(intervals)):
    if(intervals[i][0] <= ans[-1][1]):
      ans[-1][1] = max([ans[-1][1], intervals[i][0]])
    else:
      ans.append(intervals[i])
      
  return ans

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,4],[5,6]]
intervals = [[1,4],[2,3]]
print(merge(intervals))