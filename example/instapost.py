from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.instapost("https://www.instagram.com/p/COjHqwGhFA6/")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nCreated : {}".format(data["result"]["created"])
result += "\nCaption : {}".format(data["result"]["caption"])
result += "\nLikes : {}".format(data["result"]["likes"])
result += "\n\nPicture :\n{}".format(data["result"]["picture"])
number  = 0
result += "\n\nMedia Post"
for a in data["result"]["postData"]:
    number += 1
    if a["type"] == "image":
       result += "\n{}. Image Url : {}".format(number, a["postUrl"])
    if a["type"] == "video":
       result += "\n{}. Video Url : {}".format(number, a["postUrl"])
       result += "\nPoster Url: {}".format(a["poster"])
print(result)
