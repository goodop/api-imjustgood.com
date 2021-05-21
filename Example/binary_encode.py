import json, requests

text = "Imjustgood" # example text
headers = {"user-agent": "Justgood/5.0"}
host = "https://api.imjustgood.com/binary/text="+text
data = json.loads(requests.get(host,headers=headers).text)
result = data["result"]
print(result)
