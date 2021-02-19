import json, requests

query = "imjustgood" # example your string
data = requests.get("https://api.imjustgood.com/ascii="+query).text.split("pre")[1][1:][:-2]

print(data)
