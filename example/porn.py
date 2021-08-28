from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.porn("blonde")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Title : {}".format(data["result"]["title"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nQuality : {}".format(data["result"]["quality"])
result += "\nWatched : {}".format(data["result"]["watched"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nVideoURL :\n{}".format(data["result"]["videoUrl"])
print(result)
