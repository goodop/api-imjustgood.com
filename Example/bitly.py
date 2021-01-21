from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
url = "https://www.imjustgood.com" # example url
data = media.bitly(url)
result = data["result"]
print(result)
