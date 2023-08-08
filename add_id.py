import csv

def add_id_column(input_file, output_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Convert header row to lowercase
    header = [col.lower() for col in data[0]]

    # Add 'id' as the first element in the lowercase header row
    header.insert(0, 'id')

    # Add an 'Id' field starting from 1 for each data row
    for i, row in enumerate(data[1:], start=1):
        row.insert(0, str(i))

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data[1:])

if __name__ == "__main__":
    input_file = 'sports_schedules.csv'
    output_file = 'sports_schedules_with_id.csv'
    add_id_column(input_file, output_file)
