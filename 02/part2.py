import csv

with open('input.csv', mode='r', newline='', encoding='utf-8') as file:
  csv_reader = csv.reader(file)
  invalid_ids = []

  # Read the file
  for row in csv_reader:
    for item in row:
      # Get the first and last product ID per range
      id_range = item.split('-')
      product_id = int(id_range[0])
      last_product_id = int(id_range[1])

      # Loop through the IDs within the given range
      while product_id <= last_product_id:
        product_id_string = str(product_id)
        product_id_length = len(product_id_string)

        # Check if any sequence repeats
        # Only need to max check if [0, half] equals [half, end]
        # (and [0,1] = [1,2] = ... = [end-1,end])
        # (and [0,2] = [2,4] = ... = [end-2,end])
        # (up to [0,half], [half,end])
        half_length = int(product_id_length/2)
        index = 1

        while index <= half_length:
          partial = product_id_string[0:index]

          # Remove all occurances of the partial from the string
          leftover = product_id_string.replace(partial, '')

          # If there is nothing left, it means the sequence repeats
          # Add to the invalid ids and stop checking the current ID
          if leftover == '':
            invalid_ids.append(product_id)
            break
          
          # If it's not a match, check the next parial in the ID
          index += 1
        
        # Go to next item in the ID list
        product_id += 1

  # Create a sum of all invalid IDs
  invalid_sum = sum(invalid_ids)

  # Print result
  print('⭐️ Sum of invalid IDs is', invalid_sum)
