from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.tinyurl("https://www.imjustgood.com")
result = data["result"]

print(result)
