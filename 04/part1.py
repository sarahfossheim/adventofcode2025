import csv
import calculations

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)

  roll_grid = []
  counter = 0

  # Create a grid of 0 (no roll) and 1 (roll)
  for row in csv_reader:
    tonumbers = row[0].replace('@','1').replace('.','0')
    row_arr = [int(nr) for nr in list(tonumbers)]
    roll_grid.append(row_arr)

  # Loop through all the cells in the grid
  for row_index, row in enumerate(roll_grid):
    for roll_index, roll in enumerate(row):
      current_roll = roll

      # If there is a roll, count its neighbors
      if current_roll > 0:
        neighbors = calculations.count_neighbors(roll_grid, row_index, roll_index)
        
        # If there are less than 4 neighbors, add to counter
        if neighbors < 4:
          counter += 1

  # Print the result
  print('⭐️ Result:', counter)

