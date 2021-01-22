import json, requests

calculated = "10+10x10:10-10" # example multiplication
host = "https://api.imjustgood.com/calc="+calculated
data = json.loads(requests.get(host).text)
result = data["result"]

print(result)
