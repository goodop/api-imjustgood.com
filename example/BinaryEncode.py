from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.BinaryEncode("hahaha")
result = data["result"]

print(result)
