#!/usr/bin/env python
'''
8. Write a Python program using ciscoconfparse that parses this config file. Note, this config file is not fully valid (i.e. parts of the configuration are missing). The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.
'''
from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")
cont=0
for i in crypto_map:
    print crypto_map[cont].text
    for child in crypto_map[cont].children:
        print child.text
    cont+=1


