import json

# Function to export data to a JSON file
def export_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Function to import data from a JSON file
def import_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Example usage
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Export data to a JSON file
export_data(data, 'data.json')

# Import data from a JSON file
imported_data = import_data('data.json')

# Print the imported data
print(imported_data)