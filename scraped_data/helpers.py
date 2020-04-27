import json

f = open('web_scraped_data.json')
arr = json.load(f)
f.close()

professors = set()

for x in arr:
    professors.add(x['instructor'])

print(professors)