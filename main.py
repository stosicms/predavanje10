import json
from methods import load_file, save_file, delete_file, empty_file

data = load_file("data/user.json")

print(data)


data.append(
    {
    "name" : "Milos Simkovic",
    "age" : 44,
    "height" : 172,
    "gender" : "male"
}
)

save_file("data/user.json", data)
print(data)
