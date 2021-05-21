import json, requests

host = "https://api.imjustgood.com/language/code"
headers = {"user-agent": "JustGood/5.0"}
data = json.loads(requests.get(host,headers=headers).text)
result = "Language Code :"
for a in data:
    result += "\n{}".format(a)
print(result)
