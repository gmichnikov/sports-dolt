import csv
from datetime import datetime

# Function to convert date format
def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, "%B %d, %Y")
    return date_obj.strftime("%m/%d/%y")

# Read nflteams.csv and create a dictionary of team names and their corresponding city and state
teams_info = {}
with open('nflteams.csv', 'r') as teams_file:
    teams_reader = csv.DictReader(teams_file)
    for row in teams_reader:
        team_name = row['Team Name']
        city = row['City']
        state = row['State']
        teams_info[team_name] = (city, state)

# Read nfl_simplified.csv and create the combined CSV
combined_data = []
with open('nfl_simplified.csv', 'r') as schedule_file:
    schedule_reader = csv.DictReader(schedule_file)
    for row in schedule_reader:
        date = convert_date_format(row['Date'])
        home_team = row['Home Team']
        road_team = row['Road Team']

        city, state = teams_info.get(home_team, ('', ''))

        combined_data.append({
            'Date': date,
            'Home Team': home_team,
            'Road Team': road_team,
            'City': city,
            'State': state,
            'League': 'NFL',
            'Sport': 'Football'
        })

# Write the combined data to a new CSV named combined_nfl.csv
fieldnames = ['Date', 'Home Team', 'Road Team', 'City', 'State', 'League', 'Sport']
with open('combined_nfl.csv', 'w', newline='') as combined_file:
    writer = csv.DictWriter(combined_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(combined_data)

print("NFL data combined and saved in combined_nfl.csv.")
