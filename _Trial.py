import re

text = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
domain = re.findall('@(\S+)', text)
print (domain[0])

email = re.findall( '\S+?@\S+', text)
print(email)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)