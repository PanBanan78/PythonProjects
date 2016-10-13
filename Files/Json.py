__author__ = 'Oskar'

import json

json_string = '{"first_name": "Oskar", "last_name": "Matacz"}'

parsed_json = json.loads(json_string)

print(parsed_json["first_name"])