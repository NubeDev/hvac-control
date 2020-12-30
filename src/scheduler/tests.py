
import json

with open('test-payload-from-dashboard.json') as json_file:
    data = json.load(json_file)
    print(type(json_file))
    # for p in data['weekly']:
    for p in data:
        print(p)


def is_json_key_present(json, key):
    try:
        json[key]
    except KeyError:
        return False
    return True
