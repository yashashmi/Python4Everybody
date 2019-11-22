# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

sender = list()
hours = list()
maxhours = dict()

for line in handle:
    if(line.strip().startswith('From')):
        strippedline = line.strip()
        if strippedline.find('From:') > -1:
            continue
        sender.append(line.strip())

for item in sender:
    hours.append(item.split()[5].split(':')[0])

for hour in hours:
    maxhours[hour] = maxhours.get(hour, 0)+1

for k, v in sorted(maxhours.items()):
    print(k, v)