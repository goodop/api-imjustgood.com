from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.B64Encode("hahaha")
result = data["result"]

print(result)
