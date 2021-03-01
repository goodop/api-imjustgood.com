import json, requests

text = "imjustgood" # example your text
host = "https://api.imjustgood.com/ascii="+text
data = requests.get(host).text.split("pre")[1][1:][:-2]

print(data)
