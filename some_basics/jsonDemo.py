import json

# json to dicts

simple_json = '{"name": "ziya", "age": 33, "phone": "05352229285"}'

my_dict = json.loads(simple_json)

print(my_dict, type(my_dict))

print(my_dict["name"])

# dict to json

car = {"name": "farrary", "year": 2023, "model": "tuch"}

my_json = json.dumps(car)

print(my_json, type(my_json))
