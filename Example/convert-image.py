from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
image = "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" # Required base64 data (up to 32 MB)
data = media.imgurl(image)

# Get attributes
result = "Image URL : {}".format(data["result"])
print(result)

# Get JSON results
print(data)
