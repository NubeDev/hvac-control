

import json

with open('test-payload-from-dashboard.json') as json_file:
    data = json.load(json_file)
    print(json_file)
    for p in data['weekly']:
        print(p)


def is_json_key_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False

    return True