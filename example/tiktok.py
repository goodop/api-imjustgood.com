from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.tiktok("maymii69")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nFollowers : {}".format(data["result"]["followers"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\nLikes : {}".format(data["result"]["likes"])
result += "\nVideos : {}".format(data["result"]["videos"])
result += "\n\nProfile : {}".format(data["result"]["profileUrl"])
result += "\n\nPicture : {}".format(data["result"]["pictureUrl"])
result += "\n\nLastpost :"
result += "\n- Page : {}".format(data["result"]["lastpost"]["pageUrl"])
result += "\n- Thumbnail : {}".format(data["result"]["lastpost"]["poster"])
result += "\n- VideoURL : {}".format(data["result"]["lastpost"]["videoUrl"])
print(result)
