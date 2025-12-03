import csv

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)

  # What will be the result
  battery_sum = 0

  for row in csv_reader:
    # Get an array of characters in the bank
    bank = row[0]
    bank_list = list(bank) # if ints: [int(battery) for battery in list(bank)]

    # Get largest number
    # Disregard the last item of the bank, since we need double digits
    last_id = len(bank_list) - 1
    largest = max(bank_list[:last_id])
    largest_id = bank_list.index(largest)

    # Get the largest number that comes after
    largest_2 = max(bank_list[largest_id+1:])

    # Convert both to a number
    battery = largest + largest_2
    battery = int(battery)

    # Add to the sum (result)
    battery_sum += battery

  # Print result
  print('⭐️ Battery sum:', battery_sum)