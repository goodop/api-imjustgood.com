import json, requests

host = "https://api.imjustgood.com/language/code"

data = json.loads(requests.get(host).text)
result = "Language Code :"
for a in data:
    result += "\n{}".format(a)
print(result)
