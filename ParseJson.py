import json
import urllib.request, urllib.parse, urllib.error
import ssl

sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
content = urllib.request.urlopen(url, context=ctx)
data = content.read()

print('Retrieved', len(data), 'characters')

info = json.loads(data)
for comment in info['comments']:
    sum += int(comment['count'])

print(sum)