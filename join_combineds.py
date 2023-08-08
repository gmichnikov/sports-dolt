import csv

# Function to read a CSV file and return the data as a list of dictionaries
def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to write a list of dictionaries to a CSV file
def write_csv(file_name, data, fieldnames):
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Read the three combined CSV files
mls_data = read_csv('combined.csv')
mlb_data = read_csv('combined_mlb.csv')
nfl_data = read_csv('combined_nfl.csv')

# Combine the data into a single list
combined_data = mls_data + mlb_data + nfl_data

# Define the fieldnames for the combined CSV
fieldnames = ['Date', 'Home Team', 'Road Team', 'City', 'State', 'League', 'Sport']

# Normalize fieldnames in each data set to match the defined fieldnames
for data_set in [mls_data, mlb_data, nfl_data]:
    for row in data_set:
        for key in list(row.keys()):
            new_key = key.strip().title()
            if new_key != key:
                row[new_key] = row.pop(key)

# Write the combined data to sports_schedules.csv
write_csv('sports_schedules.csv', combined_data, fieldnames)

print("All sports schedules combined and saved in sports_schedules.csv.")
