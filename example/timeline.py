from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.timeline("https://timeline.line.me/post/_dYzCumD5eS8O1hq9aFKBaFHwN6dX80SeSE06k6U/1162494674404019031")
print(data)

# GET CERTAIN ATTRIBUTES
result  = "Display name : {}".format(data["result"]["displayName"])
result += "\nLike : {}".format(data["result"]["like"])
result += "\nShare : {}".format(data["result"]["share"])
result += "\n\nCaption : {}".format(data["result"]["caption"])
result += "\n\nPicture :\n{}".format(data["result"]["pictureUrl"])
if data["result"]["timeline"] != []:
   number  = 0
   result += "\n\nMedia Post :"
   for a in data["result"]["timeline"]:
       number += 1
       if a["type"] == "image":
          result += "\n{}. {}".format(number,a["url"])
       if a["type"] == "video":
          result += "\n{}. {}".format(number,a["url"])
          result += "\nThumbnail : {}".format(a["thumbnail"])
print(result)
