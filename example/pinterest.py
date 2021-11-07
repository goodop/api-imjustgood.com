from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.pinterest("https://pin.it/4jecqMl")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
for x in data["result"]:
    if x["type"] == "mp4":
        result  = "Type : Video"
        result += "\nCover : {}".format(x["cover"])
        result += "\nURL : {}".format(x["url"])
        print(result)
    elif x["type"] == "gif":
        result  = "Type : GIF"
        result += "\nCover : {}".format(x["url"])
        print(result)
    elif x["type"] == "jpg":
        result  = "Type : Image"
        result += "\nCover : {}".format(x["url"])
        print(result)
