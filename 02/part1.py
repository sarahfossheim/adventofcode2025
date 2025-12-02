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

        # Split the ID in half and compare both blocks
        if product_id_length % 2 == 0:
          half = int(product_id_length/2)
          block_1 = product_id_string[0:half]
          block_2 = product_id_string[half:product_id_length]
          
          # If it's a match, add to the list
          if block_1 == block_2:
            invalid_ids.append(product_id)
        
        # Go to next item in the ID list
        product_id += 1

  # Create a sum of all invalid IDs
  invalid_sum = sum(invalid_ids)

  # Print result
  print('⭐️ Sum of invalid IDs is', invalid_sum)
