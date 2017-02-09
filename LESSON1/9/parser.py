#!/usr/bin/env python
'''
9. Find all of the crypto map entries that are using PFS group2

'''
from ciscoconfparse import CiscoConfParse
import re
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")
cont=0
for i in crypto_map:
    for child in crypto_map[cont].children:
        if "pfs group2" in child.text:
            print crypto_map[cont].text     
    cont+=1


