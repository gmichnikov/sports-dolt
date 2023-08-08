import csv

# Read the teams from nflteams.csv and store them in a set for fast look-up
teams_set = set()
with open('nflteams.csv', 'r') as teams_file:
    teams_reader = csv.DictReader(teams_file)
    for row in teams_reader:
        team_name = row['Team Name']
        teams_set.add(team_name)

# Read the schedule from nfl_simplified.csv and check if all teams are in the teams_set
missing_teams = []
with open('nfl_simplified.csv', 'r') as schedule_file:
    schedule_reader = csv.DictReader(schedule_file)
    for row in schedule_reader:
        home_team = row['Home Team']
        road_team = row['Road Team']

        if home_team not in teams_set:
            missing_teams.append(home_team)
        if road_team not in teams_set:
            missing_teams.append(road_team)

# Print the missing teams
if missing_teams:
    print("The following teams from the schedule are missing in the teams CSV:")
    for team in set(missing_teams):
        print(team)
else:
    print("All teams in the schedule are present in the teams CSV.")
