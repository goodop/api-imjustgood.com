from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.wikipedia("jakarta")
result = data["result"]

print(result)
