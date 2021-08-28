from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.watermark_text("https://example.com/image.jpg", "https://example.com/icon.png")
result = data["result"]
print(result)

# NOTE
# ICON ONLY SUPPRT PNG FILE TYPE
