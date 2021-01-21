from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.movie_quotes()
result = data["result"]
print(result)
