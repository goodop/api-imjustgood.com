from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.youtubedl("https://youtu.be/kJQP7kiw5Fk")

result  = "Title : {}".format(data["result"]["title"])
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nWatched : {}".format(data["result"]["watched"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nAudio :\n{}".format(data["result"]["audioUrl"])
result += "\n\nVideo :\n{}".format(data["result"]["videoUrl"])
result += "\n\nPage : {}".format(data["result"]["pageUrl"])
print(result)
