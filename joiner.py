import csv

def find_fc_team_name(team_name, teams_info):
    fc_team_name = f"{team_name} FC"
    if fc_team_name in teams_info:
        return fc_team_name
    return team_name

def simplify_team_name(team_name, teams_info):
    if team_name in teams_info:
        return team_name
    fc_team_name = find_fc_team_name(team_name, teams_info)
    if fc_team_name in teams_info:
        return fc_team_name
    return team_name

# Read mlsteams.csv and create a dictionary of teams with their city and state
teams_info = {}
with open('mlsteams.csv', 'r') as teams_file:
    teams_reader = csv.DictReader(teams_file)
    for row in teams_reader:
        team_name = row['Team Name']
        teams_info[team_name] = {'City': row['City'], 'State': row['State']}

# Read mls_schedule_2.csv and create a new list with modified team names
schedule_data = []
with open('mls_schedule_2.csv', 'r') as schedule_file:
    schedule_reader = csv.DictReader(schedule_file)
    for row in schedule_reader:
        home_team = row['Home Team']
        road_team = row['Road Team']

        home_team = simplify_team_name(home_team, teams_info)
        road_team = simplify_team_name(road_team, teams_info)

        home_team_info = teams_info.get(home_team)

        if home_team_info:
            row['city'] = home_team_info['City']
            row['state'] = home_team_info['State']

        row['league'] = 'MLS'
        row['sport'] = 'Soccer'

        schedule_data.append(row)

# Write the modified data to combined.csv file
fieldnames = ['Date', 'Home Team', 'Road Team', 'city', 'state', 'league', 'sport']
with open('combined.csv', 'w', newline='') as combined_file:
    writer = csv.DictWriter(combined_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(schedule_data)

print("Data merged and saved in combined.csv.")
