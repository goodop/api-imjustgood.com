import json, requests

host = "https://api.imjustgood.com/calc="
calculated = "10+10x10:10-10" # example multiplication

data = json.loads(requests.get(host).text)
result = data["result"]

print(result)
