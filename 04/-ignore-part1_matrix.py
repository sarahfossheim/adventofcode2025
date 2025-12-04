# Something is wrong here
# Returns the correct answer for the sample
# But too low for the actual input

import csv
import numpy as np

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)

  roll_grid = []
  counter = 0

  for row in csv_reader:
    tonumbers = row[0].replace('@','1').replace('.','0')
    row_arr = [int(nr) for nr in list(tonumbers)]
    roll_grid.append(row_arr)
  
  roll_matrix = np.array(roll_grid)
  
  print('input')
  print(roll_matrix)

  all_matrices = []

  # Left
  roll_matrix_shiftL = np.roll(roll_matrix, -1, axis=1)
  roll_matrix_shiftL[:,-1] = 0
  all_matrices.append(roll_matrix_shiftL)

  # Right'
  roll_matrix_shiftR = np.roll(roll_matrix, 1, axis=1)
  roll_matrix_shiftR[:,0] = 0
  all_matrices.append(roll_matrix_shiftR)

  # Up
  roll_matrix_shiftU = np.roll(roll_matrix, -1, axis=0)
  roll_matrix_shiftU[-1,:] = 0
  all_matrices.append(roll_matrix_shiftU)

  # Down
  roll_matrix_shiftD = np.roll(roll_matrix, 1, axis=0)
  roll_matrix_shiftD[0,:] = 0
  all_matrices.append(roll_matrix_shiftD)

  # Up left
  roll_matrix_shiftUL = np.roll(roll_matrix_shiftL, -1, axis=0)
  roll_matrix_shiftUL[-1,:] = 0
  all_matrices.append(roll_matrix_shiftUL)

  # Up right
  roll_matrix_shiftUR = np.roll(roll_matrix_shiftR, -1, axis=0)
  roll_matrix_shiftUR[-1,:] = 0
  all_matrices.append(roll_matrix_shiftUR)

  # Down left
  roll_matrix_shiftDL = np.roll(roll_matrix_shiftL, 1, axis=0)
  roll_matrix_shiftDL[0,:] = 0
  all_matrices.append(roll_matrix_shiftDL)

  # Down right
  roll_matrix_shiftDR = np.roll(roll_matrix_shiftR, 1, axis=0)
  roll_matrix_shiftDR[0,:] = 0
  all_matrices.append(roll_matrix_shiftDR)

  sum_matrixes = sum(all_matrices)

  for row_index, row in enumerate(sum_matrixes):
    for roll_index, rolls in enumerate(row):
      product = int(rolls * roll_grid[row_index][roll_index])
      if product < 4 and product > 0:
        counter += 1
      # product = [int(rolls * roll_grid[row_index][i]) for i, rolls in enumerate(row)]

  print(counter)
    
