from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.customlink("example_text", "https://example.com")
result = data["result"]

print(result)
