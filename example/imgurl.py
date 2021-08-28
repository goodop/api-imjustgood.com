from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.imgurl("Image/example.jpg")
result = data["result"]

print(result)
