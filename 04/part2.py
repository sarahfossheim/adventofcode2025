import csv
import calculations

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)

  roll_grid = []
  can_remove = True
  total_counter = 0

  # Create a grid of 0 (no roll) and 1 (roll)
  for row in csv_reader:
    tonumbers = row[0].replace('@','1').replace('.','0')
    row_arr = [int(nr) for nr in list(tonumbers)]
    roll_grid.append(row_arr)

  # Loop through all the cells in the grid
  updated_grid = roll_grid[:]

  # Keep removing rolls from the grid
  while can_remove == True:
    # Reset this round's counter to 0
    counter = 0

    # Loop through all the rows in the grid
    for row_index, row in enumerate(roll_grid):
      # Make a copy of the row
      updated_row = row[:]

      # Loop through all the rolls in the row
      for roll_index, roll in enumerate(row):

        # If there is a roll, count its neighbors
        if roll > 0:
          neighbors = calculations.count_neighbors(roll_grid, row_index, roll_index)
          
          # If there are less than 4 neighbors:
          # - Add to this round's counter
          # - Add to the global counter
          # - Remove the roll from the row
          if neighbors < 4:
            updated_row[roll_index] = 0
            counter += 1
            total_counter += 1

      # Update grid after all rolls in the row have been counted and removed
      updated_grid[row_index] = updated_row
    
    # Stop the loop if no rolls were removed during the round
    if counter == 0:
      can_remove = False
    
    # Update the grid for the next round
    roll_grid = updated_grid

print('⭐️ Total rolls removed', total_counter)