import json


def save(obj, path='patientData.json'):
    print("Saving to file")
    with open(path, 'w') as json_file:
        json.dump(obj, json_file, sort_keys=True, indent=4, separators=(',', ': '))


def load(path='patientData.json'):
    try: 
        with open(path) as f:
            return json.load(f)
    except IOError:
        return load_default()


def load_default(path='patientData_default.json'):
    with open(path) as f:
        return json.load(f)


def printjson(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))
