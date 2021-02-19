import json, requests

query = "imjustgood" # example your string
data = requests.get("https://api.imjustgood.com/ascii="+query).text

print(data)
