# Count the neighbors of a coordinate in the grid
def count_neighbors(grid, row_index, col_index):
  # Collect all the neighbors
  neighbors = []

  # Get the index of the previous and next row
  row_top = row_index - 1
  row_bottom = row_index + 1

  # Get the index of the previous and next column
  col_left = col_index - 1
  col_right = col_index + 1

  # Combine the rows and cols to check in an array
  rows = [row_index, row_top, row_bottom]
  cols = [col_index, col_left, col_right]

  # Loop through all the coordinates
  for row in rows:
    for col in cols:
      
      # Ignore the original coordinates = only count neighbors
      if not (row == row_index and col == col_index):
        
        # Check if the row is within bounds
        row_exists = row >= 0 and row < len(grid)
        if row_exists:
          
          # Check if the column is within bounds
          col_exists = col >= 0 and col < len(grid[row])
          if col_exists:
            
            # If the cell exists, add it to the neighbors
            neighbors.append(grid[row][col])
  
  # Count all the neighboring rolls
  return sum(neighbors)

