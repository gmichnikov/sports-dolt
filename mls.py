import csv
from bs4 import BeautifulSoup

# Read the HTML content from the file
with open('mls.html', 'r', encoding='utf-8') as file:
    html_data = file.read()

# Replace all occurrences of '&nbsp;' with a space ' '
html_data_cleaned = html_data.replace('&nbsp;', ' ')

# Parse the cleaned HTML data
soup = BeautifulSoup(html_data_cleaned, 'html.parser')

# Find all the <ul> elements with class="tagStyle_z4kqwb-o_O-style_1y7hs1c-o_O-style_1pinbx1-o_O-style_48hmcm"
ul_elements = soup.find_all('ul', class_='tagStyle_z4kqwb-o_O-style_1y7hs1c-o_O-style_1pinbx1-o_O-style_48hmcm')

# Initialize lists to store parsed data
dates = []
home_teams = []
road_teams = []

# Loop through each <ul> element
for ul in ul_elements:
    # Find all the list items (li elements) within the <ul> tag
    list_items = ul.find_all('li')
    
    # Loop through each list item and extract the data
    for item in list_items:
        # Split the text content on the first occurrence of " - " to separate date and teams
        date, teams = item.text.strip().split(' - ', 1)
        # Split teams based on " - " or " = " to separate home and road teams
        if ' - ' in teams:
            home_team, road_team = teams.split(' - ')
        else:
            home_team, road_team = teams.split(' = ')
        # Append extracted data to respective lists
        dates.append(date.strip())
        home_teams.append(home_team.strip())
        road_teams.append(road_team.strip())

# Create and write data to CSV file
with open('mls_schedule.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header row with column names
    csv_writer.writerow(['Date', 'Home Team', 'Road Team'])
    
    # Write data rows
    for i in range(len(dates)):
        csv_writer.writerow([dates[i], home_teams[i], road_teams[i]])

print("CSV created successfully.")
