from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
userId = "the.autobots_corp" # example instagram id
data = media.instagram(userId)

if data["result"]["private"] == False:
   private = "Disable"
else:
   private = "Enable"

result = "Instagram Profile"
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nPrivate : {}".format(private)
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
        result += "\n{}. {} ( {} )".format(number, a["url"], a["created"])
        result += "\n    Page : {}".format(a["page"])

print(result)
