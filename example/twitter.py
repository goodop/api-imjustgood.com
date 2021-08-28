from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.twitter("rendytr_")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nTweet : {}".format(data["result"]["tweet"])
result += "\nFollower : {}".format(data["result"]["follower"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\n\nAvatar :\n{}".format(data["result"]["avatar"])
result += "\n\nBanner :\n{}".format(data["result"]["banner"])
print(result)
