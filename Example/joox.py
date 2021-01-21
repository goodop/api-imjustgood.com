from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "lathi" # example query
data = media.joox(query)

# Get attributes
result = "Joox Music"
result += "\nSinger : {}".format(data["result"]["singer"])
result += "\nTitle : {}".format(data["result"]["title"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nSize : {}".format(data["result"]["size"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nMp3 :\n{}".format(data["result"]["mp3Url"])
print(result)

# Get JSON results
print(data)
