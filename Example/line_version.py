import json, requests

host = "https://api.imjustgood.com/line"
data = json.loads(requests.get(host).text)

# Get attributes
result = "LINE APP VERSION"
for a in data["result"]:
    result += "\n{} : {}".format(a,data["result"][a])
print(result)

# Get JSON results
print(data)
