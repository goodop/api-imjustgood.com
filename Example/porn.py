from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "blonde" # example query
data = media.porn(query)

# Get attributes
result = "Porn Videos"
result += "\nTitle : {}".format(data["result"]["title"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nQuality : {}".format(data["result"]["quality"])
result += "\nWatched : {}".format(data["result"]["watched"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nVideo URL :\n{}".format(data["result"]["videoUrl"])
print(result)

# Get JSON results
print(data)
