#!/usr/bin/env python
'''
10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.

'''
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse('cisco_ipsec.txt')

for config_line in cisco_cfg.find_objects(r"^crypto map CRYPTO"):
    for child in config_line.children:
        if "set transform-set" in child.text and "AES" not in child.text:
            print "{0} has matching child with text '{1}' on line {2}".format(
                config_line.text, child.text, child.linenum
            )
