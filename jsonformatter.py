import json
json_data = open("links.json").read()

data = json.loads(json_data)
print(len(data))

f = open('links.txt', 'w')

for i in range(len(data)-1,-1,-1):
    f.write(data[i]["url"]+"\n")
f.close()
