import json, requests

text = "Imjustgood" # example text
host = "https://api.imjustgood.com/binary/text="+text
data = json.loads(requests.get(host).text)
result = data["result"]
print(result)
