from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.cctvSearch("204")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "CCTV CAMERA INFO"
result += "\nArea : {}".format(data["result"]["area"])
result += "\nWilayah : {}".format(data["result"]["wilayah"])
result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
result += "\n\nVideo : {}".format(data["result"]["video"])
result += "\n\n{}".format(data["result"]["camera"])
print(result)
