from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
youtube_url = "https://youtu.be/kJQP7kiw5Fk"
data = media.youtubedl(youtube_url)

result = "Youtube"
result += "\nTitle : {}".format(data["result"]["title"])
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nWatched : {}".format(data["result"]["watched"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nAudio :\n{}".format(data["result"]["audioUrl"])
result += "\n\nVideo :\n{}".format(data["result"]["videoUrl"])

print(result)
