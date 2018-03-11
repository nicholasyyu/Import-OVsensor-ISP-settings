# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

text_file = open("exposure.txt", "r")
lines = text_file.read().replace(";", "")
lines = lines.split()
print(lines)
print()
print('number of lines:', len(lines))
print()
text_file.close()
i = 0
j = 0
address = []
value = []
for i in range(0, len(lines)):
    if lines[i] == '48':
        address.append(lines[i+1])
        value.append(lines[i+2])
        i += 3
print(address)
print()
print(value)
print()

reverse_address = []
for i in reversed(address):
    reverse_address.append(i)
print(reverse_address)