from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.watermark_text("https://example.com/image.jpg", "IMJUSTGOOD")
result = data["result"]

print(result)
