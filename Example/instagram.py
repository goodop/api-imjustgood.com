from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
userId = "the.autobots_corp" # example instagram id
data = media.instagram(userId)

# Get attributes
result = "Instagram Profile"
result += "\nUsername : {}".format(data["result"]["id"])
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nWebsite : {}".format(data["result"]["website"])
result += "\nPrivate : {}".format(data["result"]["private"])
result += "\nVerified : {}".format(data["result"]["verified"])
result += "\nPost : {}".format(data["result"]["post"])
result += "\nFollower : {}".format(data["result"]["follower"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\n\nPicture :\n{}".format(data["result"]["picture"])
result += "\n\nProfile :\n{}".format(data["result"]["profile"])
if data["result"]["lastpost"] != []:
    number = 0
    result += "\n\nLastpost"
    for a in data["result"]["lastpost"]:
        number += 1
        result += "\n{}. {}".format(number, a["caption"])
        result += "\n{}".format(a["url"])
        result += "\n   Like : {}".format(number, a["like"])
        result += "\n   Comment : {}".format(number, a["comment"])
        result += "\n   Created : {}".format(a["created"])
        result += "\n   PageUrl : {}".format(a["page"])
print(result)

# Get JSON results
print(data)
