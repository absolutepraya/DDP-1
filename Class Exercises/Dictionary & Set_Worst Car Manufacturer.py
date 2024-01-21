with open('list_worst_cars.txt', 'r') as file:
    contents = file.read().splitlines()

database = {}
for element in contents:
    parts = element.split()
    manufacturer = parts[1]
    year = parts[0]
    model = " ".join(parts[2:]) if len(parts) > 2 else None
    # Makes a new dict with manufacturer as key and empty list as value if it has not been added yet
    if manufacturer not in database:
        database[manufacturer] = []
    # Appends the year and model into the dict
    database[manufacturer].append((year, model))

def find_max_mfr(dict):
    max_mfr = None
    max_count = 0
    for manufacturer, cars in dict.items():
        if len(cars) > max_count:
            max_count = len(cars)
            max_mfr = manufacturer
    return max_mfr

max_mfr = find_max_mfr(database)
print(f"The worst manufacturer is {max_mfr} 🤣🤣🤣")