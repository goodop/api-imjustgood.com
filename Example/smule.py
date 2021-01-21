from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
userId = "avamax" # example smule id
data = media.smule(userId)

# Get profile attributes
result = "Smule Profile"
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nAvatar : {}".format(data["result"]["avatar"])
number = 0
result += "\n\nRecording : "
for a in data["result"]["recording"]:
    number += 1
    result += "\n{}. {}".format(number, a["title"])
total = len(data["result"]["recording"])
result += "Total {} Recording.".format(total)
print(result)

# Get recording attributes
select_ = 1
recording = data["result"]["recording"]
list_recording = [a for a in recording]
track = list_recording[select_-1]
result = "Title : {}".format(track["title"])
result += "\nArtist : {}".format(track["artist"])
result += "\nType : {}".format(track["type"])
result += "\nPerformance : {}".format(track["performance"])
result += "\nLoves : {}".format(track["loves"])
result += "\nListens : {}".format(track["listens"])
result += "\nCreated : {}".format(track["created"])
result += "\n\nCaption :\n{}".format(track["caption"])
result += "\n\nThumbnail :\n{}".format(track["thumbnail"])
if track["type"] == "audio":
    result += "\n\Mp3 :\n{}".format(track["mp3Url"])
if track["type"] == "video":
    result += "\n\nMp4 :\n{}".format(track["mp4Url"])
print(result)

# Get JSON results
print(data)
