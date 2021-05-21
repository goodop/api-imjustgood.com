import json, requests

text = "imjustgood" # example your text
headers = {"user-agent": "Justgood/5.0"}
host = "https://api.imjustgood.com/ascii="+text
data = requests.get(host,headers=headers).text.split("pre")[1][1:-2]

print(data)
