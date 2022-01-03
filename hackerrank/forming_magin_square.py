def formingMagicSquare(s):
  # Write your code here
    row = 0
    col = 0

    # nums_set = set(s)
    # new_l = []
    row_l = []
    col_l = []
    for i in range(len(s)):
      for j in range(len(s[i])):
        col += s[j][i]
        row += s[i][j]
      print(col)
      print('row' + str(row))
      if col != 15:
        col_l.append(i)
      if row != 15:
        row_l.append(j)
      col = 0
      row = 0
    # print(col_l)
    # print(row_l)
          
##############################################
l = [
  [5,3,4],
  [1,5,8],
  [6,4,2]
]

formingMagicSquare(l)