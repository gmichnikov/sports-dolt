import csv

def update_team_name(team_name):
    team_mapping = {
        'CF Montreal': 'CF Montréal',
        'Colorado Rapid': 'Colorado Rapids',
        'DC United': 'D.C. United',
        'LAFC': 'Los Angeles FC',
        'Orlando City': 'Orlando City SC',
        'Sporting KC': 'Sporting Kansas City',
        'St. Louis City': 'St. Louis City SC'
    }
    return team_mapping.get(team_name, team_name)

# Read mls_schedule_2.csv and update team names
updated_schedule_data = []
with open('mls_schedule_2.csv', 'r') as schedule_file:
    schedule_reader = csv.DictReader(schedule_file)
    for row in schedule_reader:
        row['Home Team'] = update_team_name(row['Home Team'])
        row['Road Team'] = update_team_name(row['Road Team'])
        updated_schedule_data.append(row)

# Write the updated data back to mls_schedule_2.csv file
fieldnames = ['Date', 'Home Team', 'Road Team']
with open('mls_schedule_2.csv', 'w', newline='') as updated_schedule_file:
    writer = csv.DictWriter(updated_schedule_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_schedule_data)

print("Team names updated and saved in mls_schedule_2.csv.")
