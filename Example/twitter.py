from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
userId = "rendytr_" # example twitter id
data = media.twitter(userId)

# Get attributes
result = "Twitter Profile"
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nTweet : {}".format(data["result"]["tweet"])
result += "\nFollower : {}".format(data["result"]["follower"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\n\nAvatar :\n{}".format(data["result"]["avatar"])
result += "\n\nBanner :\n{}".format(data["result"]["banner"])
print(result)

# Get JSON results
print(data)
