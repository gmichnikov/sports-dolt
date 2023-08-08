import csv

# Function to simplify date format from "Day,Month Day" to "Month Day, Year"
def simplify_date(date_str):
    month_day = date_str.strip()
    if month_day.startswith("January"):
        year = '2024'  # Set January dates to 2024
    else:
        year = '2023'  # Set all other dates to 2023
    return f"{month_day}, {year}"

# Read the original CSV file
with open('nflfull.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Extract the relevant data (Home Team, Road Team, and Simplified Date)
simplified_data = []
for row in data:
    home_team = row['HomeTm']
    road_team = row['VisTm']
    date = simplify_date(row['Date'])
    simplified_data.append({'Home Team': home_team, 'Road Team': road_team, 'Date': date})

# Write the simplified data to a new CSV file
fieldnames = ['Home Team', 'Road Team', 'Date']
with open('nfl_simplified.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(simplified_data)

print("CSV conversion completed.")
