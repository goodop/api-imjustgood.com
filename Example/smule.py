from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
userId = "avamax" # example smule id
data = media.smule(userId)

# Get profile attributes
result = "Smule Profile"
result += "\n\nAccount Id : {}".format(data["result"]["accountId"])
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nLocation : {}".format(data["result"]["location"])
result += "\nFollowers : {}".format(data["result"]["followers"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\nRecording : {}".format(data["result"]["recording"])
result += "\nVIP : {}".format(data["result"]["vip"])
result += "\nVerified : {}".format(data["result"]["verified"])
result += "\nProfile URL : {}".format(data["result"]["profileUrl"])
result += "\nPicture URL : {}".format(data["result"]["pictureUrl"])
if data["result"]["lastpost"] != []:
    number = 0
    result += "\n\nLastpost :"
    for i in data["result"]["lastpost"]:
        number += 1
        result += "\n  {}. {}".format(number,i["title"])
print(result)

# Get lastpost attributes
postcount = 1 # count number of lastpost
lastpost = data["result"]["lastpost"][postcount-1]
result = "Title : {}".format(lastpost["title"])
result += "\nArtist : {}".format(lastpost["artist"])
result += "\nType : {}".format(lastpost["type"])
result += "\nCollabs : {}".format(lastpost["performances"])
result += "\nCreated : {}".format(lastpost["created"])
result += "\nListens : {}".format(lastpost["listens"])
result += "\nLoves : {}".format(lastpost["loves"])
result += "\nGifts : {}".format(lastpost["gifts"])
result += "\nComments : {}".format(lastpost["comments"])
result += "\nCaption :\n{}".format(lastpost["caption"])
if lastpost["type"] == "video":
    result += "\nThumbnail : {}".format(lastpost["thumbnail"])
    result += "\nVideo URL :\n{}".format(lastpost["videoUrl"])
result += "\nAudio URL :\n{}".format(lastpost["audioUrl"])
print(result)

# Get JSON results
print(data)
