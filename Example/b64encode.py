import json, requests

text = "TheAutobotsCorp" # example text
host = "https://api.imjustgood.com/base64/text="+text
data = json.loads(requests.get(host).text)
result = data["result"]
print(result)
