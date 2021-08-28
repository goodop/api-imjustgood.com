from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.B64Decode("VGhlQXV0b2JvdHNDb3Jw")
result = data["result"]

print(result)
