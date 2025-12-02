import csv

count_zero = 0
position = 50

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
    # Calculate direction
    rotation = row[0]
    direction = rotation[0]
    amount = int(rotation[1:])

    # Set the start position for this round
    start = position
    
    # Set the new position
    if direction == 'L':
      position -= amount
    elif direction == 'R':
      position += amount

    # Set the "uncorrected" position
    # Disregard the 0-99 rule for now
    position_uncorrected = position

    # If the new position is negative or 0, add an extra 100
    # This is because a result [0,-99] goes past 0 as well
    # Unless the start position is 0 (doesn't move past 0)
    if position_uncorrected <= 0 and start != 0:
      position_uncorrected -= 100

    # Calculate how many times it goes past 0
    # How many times it goes past 100 basically
    past_zero = int(abs(position_uncorrected) / 100)

    # Add to the count
    count_zero += past_zero

    # Now update the position based on the [0,99] range
    # Needed so the next loop starts from the correct point
    # If the new position is smaller than 0, go backwards from 99      
    while position < 0:
      position = 100 + position
    
    # If the new position is larger than 99, go forwards from 0
    while position > 99:
      difference = position - 99
      position = -1 + difference


  print('zeros:', count_zero)