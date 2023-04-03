import json
from glob import glob
import sys
from json_util import JsonUtil


JSON_KEY = "TimecodeBurnin"
SOURCE = sys.argv[1]
EXPECTED_QUEUE = ""

ERRORS = {
    "JSON_ERROR": {
        "message": f"The following files contain {JSON_KEY} when they should't",
        },
    "QUEUE_ERROR ": {
        "message": "The following files have a queue mismatch", 
        }
}
for key in ERRORS.keys():
    ERRORS[key]["values"] = []

json_util = JsonUtil()
for file_name in glob(SOURCE):
    with open(file_name, mode='r', encoding='utf-8') as profile:
        profile_json = json.load(profile)
        if json_util.contains_key(profile_json, JSON_KEY):
            ERRORS["JSON_ERROR"]["values"].append(file_name)
        if json_util.get_first_value(profile_json, "Queue") is EXPECTED_QUEUE:
            ERRORS["QUEUE_ERROR"]["values"].append(file_name)

print()
has_failed = False
for error in ERRORS.values():
    if error["values"]:
        has_failed = True
        print(error["message"])
        print(*error["values"], sep="/n")
        print()

if has_failed:
    sys.exit("Check Failed")
else:
    print("Success")
