import csv        # Module for working with CSV files
import random     # Module to generate random numbers
import time       # Module to control time (for delays)




# Initial values
x_value = 0       # Acts like a counter (row index)
total_1 = 1000    # Starting value for first total
total_2 = 1000    # Starting value for second total

# Define the column names for the CSV file
fieldnames = ["x_value", "total_1", "total_2"]

# Step 1: Create (or overwrite) the CSV file and write the header row
with open('data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)  # Create a writer object with column names
    csv_writer.writeheader()  # Write the first row (column titles)

# Step 2: Keep adding new rows continuously
while True:
    # Open CSV in append mode so new rows are added at the bottom
    with open('data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Create a dictionary for one row of data
        info = {
            "x_value": x_value,   # Current index
            "total_1": total_1,   # Current value of total_1
            "total_2": total_2    # Current value of total_2
        }

        # Write the row into the CSV file
        csv_writer.writerow(info)

        # Print the values on the screen (for monitoring)
        print(x_value, total_1, total_2)

    # Step 3: Update values for the next loop
    x_value += 1                          # Increment row index
    total_1 = total_1 + random.randint(-15, 10)  # Add a small random change
    total_2 = total_2 + random.randint(-14, 15)  # Add a small random change

    # Step 4: Pause execution for 1 second before adding the next row
    time.sleep(1.5)