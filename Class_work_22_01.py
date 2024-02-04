import pickle
import string
import os
import json

numbers = [1, 2, 3, 4, 5]
print(numbers)
serialized_data = pickle.dumps(numbers)
print(f"serialized data \n{serialized_data}")

deserialized_data = pickle.loads(serialized_data)
print(f"deserialized data {deserialized_data}")


def create_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(script_dir)
    return os.path.join(script_dir, file_name)


def serialize(file_name, data):
    with open(create_path(file_name), 'wb') as file:
        pickle.dump(data, file)


def deserialize(file_name):
    with open(create_path(file_name), 'rb') as file:
        data = pickle.load(file)
    return data


try:
    letters = [s for s in string.ascii_lowercase]
    print(letters)
    file_name = 'letters.dat'
    serialize(file_name, letters)
    letters_restored = deserialize(file_name)
    print(f"deserialized letters {letters_restored}")
except Exception as e:
    print(e)

capitals = {"Italy": "Rome", 'Spain': "Madrid", "Germany": "Berlin"}
print(capitals)
serialized_capitals = json.dumps(capitals)
print(f"JSON serialized: {serialized_capitals}")
deseroalized_capitals = json.loads(serialized_capitals)
print(f"deserialized capitals: {deseroalized_capitals}")


def serialize_json(file_name, data):
    path = create_path(file_name)
    with open(path, 'w') as file:
        json.dump(data, file,indent=4)


def deserialize_json(file_name):
    path = create_path(file_name)
    with open(path, 'r') as file:
        data = json.load(file)
    return data


try:
    file_name = 'employee.json'
    employee_dict = {
        "company": 'Microsoft',
        "employees": [
            {"name": "Nick",
             "age": 30,
             "department": 'Sales'},
            {"name": "Bill",
             "age": 35,
             "department": 'Marketing'}
        ]
    }

    serialize_json(file_name, employee_dict)
    deserialized_employee = deserialize_json(file_name)
    print(deserialized_employee)
except Exception as e:
    print(e)
