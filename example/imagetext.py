from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.imagetext("Welcome to Imjustgood.com")
result = data["result"]

print(result)
