import csv

# Read mlbteams.csv and create a set of team names
teams_set = set()
with open('mlbteams.csv', 'r') as teams_file:
    teams_reader = csv.DictReader(teams_file)
    for row in teams_reader:
        teams_set.add(row['Team Name'])

# Read mlb_schedule.csv and check if all team names exist in the teams CSV
missing_teams = set()
with open('mlb_schedule.csv', 'r') as schedule_file:
    schedule_reader = csv.DictReader(schedule_file)
    for row in schedule_reader:
        home_team = row['Home Team']
        road_team = row['Road Team']

        if home_team not in teams_set:
            missing_teams.add(home_team)
        if road_team not in teams_set:
            missing_teams.add(road_team)

# Print the missing team names
print("The following team names from the schedule CSV are not found in the teams CSV:")
for team_name in missing_teams:
    print(team_name)
