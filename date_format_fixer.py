import csv
import re
from datetime import datetime

def convert_date_format(date_str):
    # Input formats: 'm/d/yyyy', 'mm/dd/yyyy', 'm/dd/yyyy', 'mm/d/yyyy'
    # Output format: 'yyyy-mm-dd'
    date_formats = ['%m/%d/%Y', '%-m/%d/%Y']
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_str, date_format)
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            pass
    return None

def main():
    input_file = 'sports_schedules_with_id.csv'
    output_file = 'sports_schedules_with_id_updated.csv'

    with open(input_file, newline='') as f_input, open(output_file, 'w', newline='') as f_output:
        reader = csv.DictReader(f_input)
        fieldnames = reader.fieldnames

        # Write to the new CSV file with updated date format
        writer = csv.DictWriter(f_output, fieldnames)
        writer.writeheader()

        for row in reader:
            # Convert the date format and write the updated row to the output file
            row['game_date'] = convert_date_format(row['game_date'])
            writer.writerow(row)

if __name__ == '__main__':
    main()
