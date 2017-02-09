#!/usr/bin/env python
'''
7. Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.
'''
import yaml
import json
from pprint import pprint as nicer
with open("dump.yml") as f:
    new_list = yaml.load(f)

print "YAML FORMAT"
print yaml.dump(new_list, default_flow_style=False)

with open("dump.json") as f:
    new_list = json.load(f)
print "JSON FORMAT"
nicer(new_list)
