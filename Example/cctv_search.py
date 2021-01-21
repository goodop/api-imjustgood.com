from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
cctv_code = "204" # example cctv code
data = media.cctvSearch(cctv_code)

# Get attributes
result = "CCTV STREET CAMERA"
result += "\nArea : {}".format(data["result"]["area"])
result += "\nWilayah : {}".format(data["result"]["wilayah"])
result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
result += "\n\nVideo : {}".format(data["result"]["video"])
result += "\n\n{}".format(data["result"]["camera"])
print(result)

# Get JSON results
print(data)
