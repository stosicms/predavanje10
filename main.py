import json
from methods import load_file, save_file, delete_file

data = load_file("data/user.json")

print(data)


delete_file("data/user.json", "Milos Simkovic")
print(data)