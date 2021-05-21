import json, requests

host = "https://api.imjustgood.com/custom/make"
url = "https://cdn-0.scatteredquotes.com/wp-content/uploads/2019/07/Sad-Quotes-2-945x945.jpg" # example your url
label = "quotes" # example your custom name

headers = {"label": label, "url": url, "user-agent": "Justgood/5.0"}
data = json.loads(requests.get(host, headers=headers).text)

print(data["result"])
