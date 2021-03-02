from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
image = "Image/logo.jpg" # example your image path
data = media.imgurl(image)
result = data["result"]

print(result)
