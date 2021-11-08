from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.twitter("rendytr_")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result += "\nID : {}".format(data["result"]["id"])
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nVerified : {}".format(data["result"]["verified"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nTweet : {}".format(data["result"]["tweet"])
result += "\nMedia : {}".format(data["result"]["media"])
result += "\nFollowers : {}".format(data["result"]["follower"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\n\nAvatar :\n{}".format(data["result"]["avatar"])
result += "\n\nBanner :\n{}".format(data["result"]["banner"])
print(result)
