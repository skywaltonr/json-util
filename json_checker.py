import json
from glob import glob
import sys
from json_util import JsonUtil
JSON_KEY = "TimecodeBurnin"
SOURCE = sys.argv[1]

util = JsonUtil()
success = True
for file_name in glob(SOURCE):
    with open(file_name, mode='r', encoding='utf-8') as profile:
        profile_json = json.load(profile)
        if util.contains_key(profile_json, JSON_KEY):
            success = False
            print(file_name)
        print(util.get_first_value(profile_json, "Queue"))

if success is False:
    sys.exit("Timecode Check Failed")
