import json

data = {
    "student": {
        "name": "Arman",
        "species": "Ca de Bou",
        "group": "noname"
    }
}

with open("my_json_file.json", "w") as test_json:
    json.dump(data, test_json, indent=4)

string_data = json.dumps(data, indent=4)
print(string_data)
print(type(string_data))


# load | loads
