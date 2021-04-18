import json
import pprint

f = open('additional_data/json_parse/map.json', encoding = 'utf-8')

ff = json.load(f)

for country in ff['features']:
    pprint.pprint(country['type'])
    pprint.pprint(country['properties']['NAME'])
    pprint.pprint(str(country['geometry']['type']))
    print()

f.close()

# f = open('additional_data/json_parse/registrants.json', encoding = 'utf-8')

# ff = json.load(f)

# for student in ff['students']:

#     pprint.pprint(student['student'])
#     pprint.pprint(student['student']['domain'])

# f.close()

# f = open('additional_data/json_parse/training.json', encoding = 'utf-8')
# lst = []
# for line in f:
#     pprint.pprint(json.loads(line))
#     lst.append(json.loads(line).items())

# print(len(lst))
# print(lst)

# f.close()