import math

# 973. K Closest Points to Origin

# Time Complexity: O(n) Space Complexity: O(n) ?


def kClosest(points, k):
    points_len = len(points)
    dist = []
    ans = []
    for i in range(points_len):
        cur_distance = math.sqrt(points[i][0]**2 + points[i][1]**2)
        dist.append([cur_distance, points[i]])

    dist.sort()
    for i in range(k):
        ans.append(dist[i][1])
    return ans[:k]


# LC Discussion answer 
def kClosest2(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(kClosest(points, k))
