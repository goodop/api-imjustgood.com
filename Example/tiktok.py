from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
userId = "maymii69"
data = media.tiktok(userId)

result = "Tiktok Profile"
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nFollowers : {}".format(data["result"]["followers"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\nLikes : {}".format(data["result"]["likes"])
result += "\nPicture : {}".format(data["result"]["pictureUrl"])
result += "\nProfile : {}".format(data["result"]["profileUrl"])

print(result)
