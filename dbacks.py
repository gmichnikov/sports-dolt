import csv

# Function to replace team names
def replace_team_name(team_name):
    if team_name == "Arizona D'Backs":
        return "Arizona Diamondbacks"
    return team_name

# Read mlb_schedule.csv, modify team names, and save back to the same CSV
with open('mlb_schedule.csv', 'r') as schedule_file:
    schedule_reader = csv.DictReader(schedule_file)
    schedule_data = list(schedule_reader)

for row in schedule_data:
    row['Home Team'] = replace_team_name(row['Home Team'])
    row['Road Team'] = replace_team_name(row['Road Team'])

# Write the modified data back to mlb_schedule.csv
fieldnames = ['Home Team', 'Road Team', 'Date', 'Sport']
with open('mlb_schedule.csv', 'w', newline='') as schedule_file:
    writer = csv.DictWriter(schedule_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(schedule_data)

print("Team names updated and saved in mlb_schedule.csv.")
