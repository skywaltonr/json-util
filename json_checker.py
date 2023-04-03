import json
from glob import glob
import time
import sys
from json_util import JsonUtil
import os
print ()
JSON_KEY = "TimecodeBurnin"
SOURCE = sys.argv[1]

st = time.time()
output = []
util = JsonUtil()
for file_name in glob(SOURCE):
    with open(file_name, mode='r', encoding='utf-8') as profile:
        profile_json = json.load(profile)
        if util.contains_key(profile_json, JSON_KEY):
            output.append(file_name)
        print(util.get_first_value(profile_json, "Queue"))

et = time.time()
sys.exit(output)
elapsed_time = et - st
print('Execution time:', elapsed_time * 1000, 'ms')