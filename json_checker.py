import json
from glob import glob
import sys
from json_util import JsonUtil
JSON_KEY = "TimecodeBurnin"
SOURCE = sys.argv[1]

util = JsonUtil()
files_to_fix = []
for file_name in glob(SOURCE):
    with open(file_name, mode='r', encoding='utf-8') as profile:
        profile_json = json.load(profile)
        if util.contains_key(profile_json, JSON_KEY):
            files_to_fix.append(file_name)
            print(JSON_KEY, "Found In", file_name)

if files_to_fix:
    print("The following files failed: ")
    print(*files_to_fix, sep = "\n")
    sys.exit("Timecode Check Failed")
