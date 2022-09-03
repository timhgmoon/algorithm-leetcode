# 240. Search a 2D Matrix II

'''
1. check if matrix is empty 
2. go through each row
3. see if the target is equal to or in between the first and last element in array
4. if target equal or inbetween then use for loop to go through each element and return true if target is found
5. if go through whole loop target was not found in the matrix 
6. return false
'''

def searchMatrix(matrix, target):
  if len(matrix) == 0 or len(matrix[0]) == 0:
    return False

  for i in range(len(matrix)):
    first = matrix[i][0]
    last = matrix[i][len(matrix[i]) - 1]

    if target >= first and target <= last:
      for j in range(len(matrix[i])):
        if matrix[i][j] == target:
          return True

  return False