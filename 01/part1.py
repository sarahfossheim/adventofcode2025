import csv

count_zero = 0
position = 50

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
    rotation = row[0]
    direction = rotation[0]
    amount = int(rotation[1:])

    # Update position
    if direction == 'L':
      position -= amount
    elif direction == 'R':
      position += amount
      
    # If smaller than 0, go backwards from 99      
    while position < 0:
      position = 100 + position
    
    # If larger than 99, go forwards from 0
    while position > 99:
      difference = position - 99
      position = -1 + difference

    # If position equals 0, add to counter
    if position == 0:
      count_zero += 1

  print(count_zero)