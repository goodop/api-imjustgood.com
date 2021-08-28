from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.kbbi("komputer")
result = data["result"]["desc"]

print(result)
