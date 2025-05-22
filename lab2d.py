#!/usr/bin/env python3

import sys

#Check for exactly 2 arguments (script name +2)

if len(sys.argv) != 3:
    print('Usage:', sys.argv[0], 'name age')
    sys.exit() 
    
name = sys.argv[1]
age = int(sys.argv[2])

print("Hi " + name + ", you are " + str(age) + " years old.")