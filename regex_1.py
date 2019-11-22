import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_330919.txt"
handle = open(name)

digitresult = list()
numberlist = list()

for line in handle:
    digitresult.append(re.findall('[0-9]+', line.strip()))

for array in digitresult:
    for item in array:
        try:
            numberlist.append(int(item))
        except: 
            continue

print(len(numberlist))
print(sum(numberlist))