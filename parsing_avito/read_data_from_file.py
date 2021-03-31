import json

def read_data_from_file():
    rooms = []
    with open('rooms_file.json.json', 'r') as file:
        rooms = json.load(file)
    return json.loads(rooms)

# rooms = read_data_from_file()