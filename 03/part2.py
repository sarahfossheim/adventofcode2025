import csv

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)

  # What will be the result
  battery_sum = 0

  # Length of battery sequence
  sequence_length = 12

  for row in csv_reader:
    # Get an array of characters in the bank
    bank = row[0]
    bank_list = list(bank) # if ints: [int(battery) for battery in list(bank)]

    # Get max IDs that can be skipped
    bank_length = len(bank_list)
    skippable = bank_length - sequence_length

    # Total IDs skipped
    skipped = 0
    previous_id = -1

    # Set the chosen numbers
    chosen_batteries = []

    while len(chosen_batteries) < sequence_length:
      # Set the start ID to the previous one + 1
      start_id = previous_id + 1

      # Last ID to choose from is  [1, 2, 3] away from previous
      end_id = start_id + skippable + 1

      # Find the largest battery in the specified range
      battery_range = bank_list[start_id:end_id]
      largest = max(battery_range)

      # Get the ID the number has within the new range
      largest_id = battery_range.index(largest)

      # Get the ID the number has in the original range
      # Needed to split it up to account for repeated nrs
      largest_id_corrected = largest_id + start_id

      # Add the largest battery to the list of batteries
      chosen_batteries.append(largest)

      # Get the amount of IDs skipped in this round
      skipped = largest_id_corrected - start_id
      skippable -= skipped

      # Update the "previous id"
      previous_id = largest_id_corrected

      # If 3 items have been skipped, then add the rest of the array
      if skippable <= 0 and len(chosen_batteries) < 12:
        last_ids = largest_id_corrected + 1
        chosen_batteries.extend(bank_list[last_ids:])

    # Convert the chosen batteries array to a string
    chosen_batteries_str = ''.join(chosen_batteries)

    # Add it to the battery sum
    battery_sum += int(chosen_batteries_str)

  # Result
  print('⭐️ Sum', battery_sum)


