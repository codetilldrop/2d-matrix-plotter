# Program to parse a given matrix in matrix.txt

file = open('matrices.txt')

# matrice_plot_data will be a list which consists of 
# a dictionary per matrix in matrix.txt. A dictionary 
# will for a matrix will be in the format [x, y]: binary val
# where an [x, y] acts as the key and represents element indexes 
# and binary val is a 1 or 0 for whether a point exists
# at the given key
matrice_plot_data = []

IS_NEW_MATRIX = False
curr_matrix_row = 0
curr_matrix_col = 0

curr_matrice_idx = 0
# new_matrix(line) will check to see if an opening 
# square bracket is detected at the start of a line (passed
# as an argument) indicating a new matrix
def new_matrix (line):
  line = line.replace(" ", "")
  if "[" in line:
    global IS_NEW_MATRIX
    global curr_matrix_row
    global curr_matrix_col

    IS_NEW_MATRIX = True
    matrice_plot_data.append({})
    curr_matrix_row = 1
    curr_matrix_col = 1
    return True




for idx, line in enumerate(file):
  line = line.rstrip()
  if IS_NEW_MATRIX == False:
    new_matrix(line)

  if IS_NEW_MATRIX == True and line != "[":
    for char in line:
      if char != " " and char != "]":
        matrix = matrice_plot_data[curr_matrice_idx]
        coordinates = tuple([curr_matrix_row, curr_matrix_col])
        matrix[coordinates] = char
        curr_matrix_col += 1

    curr_matrix_row += 1
    curr_matrix_col = 1