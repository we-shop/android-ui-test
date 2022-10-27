import os
import json
import ast

dct = {
    "device": "Samsung Galaxy A51",
    "os_version": "10.0",
    "project": "First Python project2",
    "build": "browserstack-build-android",
    "name": "Android_tests",
    "app_url": "bs://d2e53d8411b48c4ca19e25dd2902acb5337e1a91",
    "appium:resetKeyboard": True,
    "autoGrantPermissions": True,
    "appium:unicodeKeyboard": True,
    "appium:noReset:": False}

os.environ['TEST'] = f'{dct}'
get_ = os.getenv("TEST")
#a = json.loads()

s = get_.replace("\'", "\"")
t = ast.literal_eval(json.dumps(s)) #json.loads(s)

parsed_json = dict(eval(t))

print(parsed_json)
print(type(parsed_json))

# to JSON
to_json = json.dumps(parsed_json, indent = 4)

print(to_json)
print(type(to_json))
############################

