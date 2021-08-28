from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.simisimi("kenapa anda jomnlo ?")
result = data["result"]

print(result)
