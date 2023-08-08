import json
import csv

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_to_csv(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write header row with column names
        csv_writer.writerow(['Home Team', 'Road Team', 'Date', 'Sport'])
        
        # Write data rows
        for event in data:
            home_team = event['competitor'][1]['name']
            road_team = event['competitor'][0]['name']
            date = event['startDate']
            sport = event['sport']
            
            csv_writer.writerow([home_team, road_team, date, sport])

if __name__ == "__main__":
    file_path = "reducedmlb.html"

    # Load JSON data from the file
    json_data = load_json_file(file_path)

    # Save the data to CSV file
    save_to_csv("mlb_schedule.csv", json_data)

    print("CSV created successfully.")
