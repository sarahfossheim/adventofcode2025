import csv

def get_ingredients(first, last):
  return last - first + 1

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)

  fresh_ingredients = []
  counted_ingredients = []
  count = 0
  
  # Create a sorted list of ranges
  for row in csv_reader:
    if row != [] and '-' in row[0]:
      fresh_range = [int(i) for i in row[0].split('-')]
      fresh_ingredients.append(fresh_range)
  
  fresh_ingredients = sorted(fresh_ingredients, key=lambda x: x[0])

  # Now compare the ranges against eachother to filter out overlap
  for checking in fresh_ingredients:
      difference = 0

      has_match = False

      match_x = [checking[0]]
      match_y = [checking[1]]

      # Compare this range to ranges already processed
      for index, existing in enumerate(counted_ingredients):
        lastID = len(existing) - 1

        # Add the smaller part
        # If the new range starts lower than existing one
        # And if the new range ends after the existing one started
        if (checking[0] <= existing[0]) and (checking[1] >= existing[0]):
          difference = get_ingredients(checking[0], existing[0] - 1)
          count += difference
          has_match = True

        
        # Add the larger part
        # If the new range ends after existing one ends
        # And if the new range starts before existing one ends
        if (checking[1] >= existing[lastID]) and (checking[0] <= existing[lastID]):
          difference = get_ingredients(existing[lastID] + 1, checking[1])
          count += difference
          has_match = True

        # If the new range falls entirely within an existing range
        if (checking[0] >= existing[0]) and (checking[1] <= existing[1]):
          has_match = True

        if has_match == True:
          match_x.append(existing[0])
          match_y.append(existing[lastID])
          counted_ingredients.remove(existing)
          counted_ingredients.append([min(match_x), max(match_y)])
        
      if has_match == False:
        difference = get_ingredients(checking[0], checking[1])
        counted_ingredients.append(checking)
        count += difference

  print('⭐️ The result is', count)
  