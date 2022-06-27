# 973. K Closest Points to Origin

# Time Complexity: O(n) Space Complexity: O(n) ?
def kClosest(points, k):
  points_len = len(points)
  dist = []
  ans = []
  for i in range(points_len):
    cur_distance = points[i][0]**2 + points[i][1]**2
    dist.append([cur_distance, i])

  dist.sort()
  for i in range(len(dist)):
    inorder_index = dist[i][1]
    ans.append(points[inorder_index])

  return ans[:k]

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))