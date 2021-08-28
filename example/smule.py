from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.smule("avamax")
print(data)

# EXAMPLE GET PROFILE ATTRIBUTES
result  = "Account Id : {}".format(data["result"]["accountId"])
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
if data["result"]["post"] != []:
    number  = 0
    result += "\n\nPerformances :"
    for i in data["result"]["post"]:
        number += 1
        result += "\n  {}. {}".format(number,i["title"])
print(result)

# EXAMPLE GET PERFORMANCES ATTRIBUTES
performances  = data["result"]["post"]
if performances == []:
    result = "Not found"
else:
    number   = 1
    main     = performances[number-1]
    download = api.smuledl(main["pageUrl"])
    result   = "Artist : {}".format(main["artist"])
    result  += "\nTitle : {}".format(main["title"])
    result  += "\nCaption : {}".format(main["caption"])
    result  += "\nCreated : {}".format(main["created"])
    result  += "\nLove : {}".format(main["loves"])
    result  += "\nGift : {}".format(main["gifts"])
    result  += "\nListen : {}".format(main["listens"])
    result  += "\nThumbnail : {}".format(main["thumbnail"])
    result  += "\nPerformances : {}".format(main["performances"])
    result  += "\nPage : {}".format(main["pageUrl"])
    result  += "\n\nAudio URL : {}".format(download["result"]["mp3Url"])
    if download["result"]["type"] == "video":
        result += "\n\nVideo URL : {}".format(download["result"]["mp4Url"])
print(result)
