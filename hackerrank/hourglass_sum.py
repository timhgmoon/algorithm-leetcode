#hackerrank - hourglassSum

'''
1. create variable to hold all arrays of total
2. will be working with a 6x6 where the hour glass is contained inside a 3x3 grid
3. need to shift right 3 times and shift down 3 times
4. first row should be total of 3 elements
5. second row should only be the element inbetween
6. third row should be total of 3 elements as well
7. get the total of all threw rows
8. append to our array
9. return the max of the array
'''

def hourglassSum(arr):
    total_arr = []
    for i in range(4):
        for j in range(4):
            first_row = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            second_row = arr[i+1][j+1]
            third_row = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            total_arr.append(first_row + second_row + third_row)
    
    return max(total_arr)

# change = [
#   [1, 1, 1, 0, 0, 0],
#   [0, 1, 0, 0, 0, 0],
#   [1, 1, 1, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0,]
# ]

change = [
  [-9, -9, -9, 1, 1, 1,], 
  [0, -9, 0, 4, 3, 2],
  [-9, -9, -9, 1, 2, 3],
  [0, 0, 8, 6, 6, 0],
  [0, 0, 0, -2, 0, 0],
  [0, 0, 1, 2, 4, 0]
 ]

print(hourglassSum(change))