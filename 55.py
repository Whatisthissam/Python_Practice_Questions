import csv
file_name = input("Enter the CSV file name to read: ")

try:
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
