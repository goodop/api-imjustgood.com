from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
userId = "maymii69" # example tiktok id
data = media.tiktok(userId)

# Get attributes
result = "Tiktok Profile\n"
result += "\nUsername : {}".format(data["result"]["username"])
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
result += "\n- Poster : {}".format(data["result"]["lastpost"]["poster"])
result += "\n- Video : {}".format(data["result"]["lastpost"]["videoUrl"])
print(result)

# Get JSON results
print(data)
