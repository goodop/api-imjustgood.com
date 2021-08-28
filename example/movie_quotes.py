from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.movie_quotes()
result = data["result"]

print(result)
