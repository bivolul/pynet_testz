#!/usr/bin/env python
'''
6. Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.

'''
import json
import yaml

my_list = range(8)
my_list.append('1020')
my_list.append('2020')
my_list.append('the sky is blue')
my_list.append({})
my_list[-1]['nothing']='nothing is still nothing'
my_list[-1]['dictionary']=range(3)
my_list[-1]['dictionary'][0]='first element'
my_list[-1]['dictionary'][1]='50'
my_list[-1]['dictionary'][2]='last element'

with open("dump.yml","w") as f:
    f.write(yaml.dump(my_list,default_flow_style=False))

with open("dump.json","w") as f:
    json.dump(my_list,f)

