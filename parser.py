# Program to parse a given matrix in matrix.txt

file = open('matrix.txt')

# matrice_plot_data will be a list which consists of 
# a dictionary per matrix in matrix.txt. A dictionary 
# will for a matrix will be in the format [x, y]: binary val
# where an [x, y] acts as the key and represents element indexes 
# and binary val is a 1 or 0 for whether a point exists
# at the given key
matrice_plot_data = []

# new_matrix(line) will check to see if an opening 
# square bracket is detected at the start of a line (passed
# as an argument) indicating a new matrix
def new_matrix (line):
  line = line.replace(" ", "")


for line in file:
  new_matrix(line)