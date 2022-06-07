
# 74. Search a 2D Matrix
def searchMatrix(matrix, target):
    
  m = len(matrix)
  n = len(matrix[0])
  index = -1
  #get the row that target should be in if target exists
  for i in range(m):
    if target <= matrix[i][n-1]:
      index = i
      break

  if index == -1:
    return False

  #check row to see if target is there
  for i in range(len(matrix[index])):
    if target ==  matrix[index][i]:
      return True

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3  # True
# target = 5  # True
# target = 4  # False (number is not inside matrix)

print(searchMatrix(matrix, target))

