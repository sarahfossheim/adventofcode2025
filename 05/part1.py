import csv

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)

  fresh = []
  check_ingredients = False

  fresh_ingredients = 0
  
  for row in csv_reader:

    # Check if ingredients are in the fresh list
    if check_ingredients == True:

      if row != []:
        ingredient = int(row[0])
        for fresh_item in fresh:
          if fresh_item[0] <= ingredient <= fresh_item[1]:
            fresh_ingredients += 1
            break
    
    # Add to fresh list as long as empty line is not met
    else:
      if row == []:
        check_ingredients = True
      elif '-' in row[0]:
        fresh.append([int(i) for i in row[0].split('-')])
    
print('⭐️  Result (amount of fresh ingredients)', fresh_ingredients)