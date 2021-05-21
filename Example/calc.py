import json, requests

calculated = "10+10x10:10-10" # example multiplication
headers = {"user-agent": "Justgood/5.0"}
host = "https://api.imjustgood.com/calc="+calculated
data = json.loads(requests.get(host,headers=headers).text)
result = data["result"]

print(result)
