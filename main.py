import json

with open("data.json", 'r') as file:
    data = json.load(file)
    data.append({
        "name" : "Jelena Mitrovic",
        "age" : 38,
        "height" : 178,
        "gender" : "female"
    })

with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)