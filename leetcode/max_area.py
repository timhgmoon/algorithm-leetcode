#Brute force
def maxArea(height):
  ans = 0
  for i in range(len(height)):
    for j in range(i + 1, len(height)):
      max_height = 0
      if(height[i] < height[j]):
        max_height = height[i]
      else:
        max_height = height[j]

      current_area = max_height * (j - i)
      if(ans < current_area):
        ans = current_area
  return ans

def maxArea(height):
  max_area = 0
  left = 0
  right = len(height) - 1

  while (left < right):
    if(height[left] < height[right]):
      max_height = height[left]
    else:
      max_height = height[right]
    current_area = max_height * (right-left)
    if max_area  < current_area:
      max_area = current_area
    if(height[left] < height[right]):
      left += 1
    else:
      right -= 1
  
  return max_area

input = [1, 8, 6, 2, 5, 4, 8, 3 , 7]
print(maxArea(input))