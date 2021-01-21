from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
post_url = "https://instagram.com/p/CJtqfEbhpjO/" # example instapost url
data = media.instapost(post_url)

# Get attributes
result = "Instagram Post"
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nCreated : {}".format(data["result"]["created"])
result += "\nCaption : {}".format(data["result"]["caption"])
result += "\n\nPicture :\n{}".format(data["result"]["picture"])
number = 0
result += "\n\nMedia Post"
for a in data["result"]["postData"]:
    number += 1
    if a["type"] == "image":
       result += "\n{}. Image Url : {}".format(number, a["postUrl"])
    if a["type"] == "video":
       result += "\n{}. Video Url : {}".format(number, a["postUrl"])
       result += "\n    Poster : {}".format(number, a["poster"])
print(result)

# Get JSON results
print(data)
