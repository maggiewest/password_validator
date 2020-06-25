#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:44:35 2020

@author: maggiewest
"""

import sys

invalid_pwds = {}

if len (sys.argv) != 2:
    print("Usage: python3 password_validator.py weak_password_list.txt")
    sys.exit(1)
    
try:
    weakfile = open(sys.argv[1])
    weak_contents = weakfile.read()
    weaklist = weak_contents.splitlines()
except IOError:
    print("Cannot read weak password list file")
finally:
    weakfile.close()

    
def check_password(pwd):
    while True:
        if not (all(ord(c) < 128 for c in pwd)):
            newpwd = "".join(map(lambda x : x if (ord(x) < 128) else "*",pwd))
            invalid_pwds.update({newpwd : "Contains non-ASCII characters"})
            break
        if (len(pwd) < 8):
            invalid_pwds.update({pwd : "Too short"}) 
            break
        if (len(pwd) > 64):
            invalid_pwds.update({pwd : "Too long"})
            break
        if (pwd in weaklist):
            invalid_pwds.update({pwd : "Too common"})
            break
        else:
            break
    


def main():
    pwdlist=[]
    while True:
        data = sys.stdin.readline().rstrip()
        if data:
            pwdlist.append(data)
            check_password(data)
        if not len(data):
            break
    for key, value in invalid_pwds.items():
        print(key + " --> Error: " + value)
           
    
    
if __name__ == "__main__":
    main()    
    
