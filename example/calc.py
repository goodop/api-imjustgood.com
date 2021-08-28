from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.calc("10+10x10:10-10")
result = data["result"]

print(result)
