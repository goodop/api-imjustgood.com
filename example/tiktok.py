from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.tiktok("maymii69")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nPrivate : {}".format(data["result"]["private"])
result += "\nVerified : {}".format(data["result"]["private"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nFollowers : {}".format(data["result"]["followers"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\nLikes : {}".format(data["result"]["likes"])
result += "\nVideos : {}".format(data["result"]["videos"])
result += "\n\nProfile : {}".format(data["result"]["profileUrl"])
result += "\n\nPicture : {}".format(data["result"]["pictureUrl"])
print(result)
if data["result"]["lastpost"] != []:
    for a in data["result"]["lastpost"]:
        result  = "\Lastpost"
        result += "\n- Caption : {}".format(a["desc"])
        result += "\n- Created : {}".format(a["created"])
        result += "\n- Comments : {}".format(a["comment"])
        result += "\n- Playing : {}".format(a["playing"])
        result += "\n- Share : {}".format(a["share"])
        result += "\n- Page : {}".format(a["pageUrl"])
        result += "\n- Thumbnail : {}".format(a["poster"])
        result += "\n- VideoURL : {}".format(a["videoUrl"])
        print(result)
