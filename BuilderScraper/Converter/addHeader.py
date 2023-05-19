import csv

# Define the headers to be added
headers = ['Article Title', 'Article Description', 'Article Author', 'Article Link', 'Article Image']

# Read the existing data from the CSV file
with open('builderOnline.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Insert the headers at the beginning of the data
data.insert(0, headers)

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)



