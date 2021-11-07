from justgood import imjustgood

api       = imjustgood("YOUR_APIKEY_HERE")
data      = api.instastory("the.goperation")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result    = "ID : {}".format(data["result"]["id"])
result   += "\nFullname : {}".format(data["result"]["fullname"])
result   += "\nUsername : {}\n".format(data["result"]["username"])
result   += "\nPicture : {}\n".format(data["result"]["picture"])
result   += "\nProfile : {}\n".format(data["result"]["profile"])
result   += "\n- List stories -"
number    = 0
for a in data["result"]["stories"]:
  number += 1
  result += "\nStories {} : {}".format(number,a["url"])
  result += "\nCreated {}".format(a["created"])
  if a["type"] == "video":
    result += "\Thumbnail : {}".format(a["thumbnail"])
print(result)
