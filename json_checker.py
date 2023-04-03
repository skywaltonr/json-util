import json
from glob import glob
import time
from json_util import JsonUtil

JSON_KEY = "TimecodeBurnin"
SOURCE = '/Users/rwo26/work/adtech-dai-media/src/config/transcode_profiles/preprod/*.json'

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

elapsed_time = et - st
print('Execution time:', elapsed_time * 1000, 'ms')
