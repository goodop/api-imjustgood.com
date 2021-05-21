import json, requests

host = "https://api.imjustgood.com/line"
headers = {"user-agent": "JustGood/5.0"}
data = json.loads(requests.get(host,headers=headers).text)

# Get attributes
result = "LINE APP VERSION"
for a in data["result"]:
    result += "\n{} : {}".format(a,data["result"][a])
print(result)

# Get JSON results
print(data)
