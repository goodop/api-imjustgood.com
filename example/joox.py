from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.joox("lathi")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Singer : {}".format(data["result"]["singer"])
result += "\nTitle : {}".format(data["result"]["title"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nSize : {}".format(data["result"]["size"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nMp3 :\n{}".format(data["result"]["mp3Url"])
print(result)
