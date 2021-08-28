from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.tiktokdl("https://www.tiktok.com/@mamayukakuroyanagi/video/6810023518508518657")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nCaption : {}".format(data["result"]["caption"])
result += "\nMusic : {}".format(data["result"]["music"])
result += "\nPlay : {}".format(data["result"]["play"])
result += "\nShare : {}".format(data["result"]["share"])
result += "\n\nPicture : {}".format(data["result"]["picture"])
result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
result += "\n\nWatermark : {}".format(data["result"]["watermark"])
result += "\n\nNo watermark : {}".format(data["result"]["no_watermark"])
print(result)
