from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.tiktokdl("https://vt.tiktok.com/ZSJ56SDPs/")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nCaption : {}".format(data["result"]["caption"])
result += "\nMusic : {}".format(data["result"]["music"])
result += "\nPlay : {}".format(data["result"]["play"])
result += "\nShare : {}".format(data["result"]["share"])
result += "\nComment : {}".format(data["result"]["comment"])
result += "\n\nPicture : {}".format(data["result"]["picture"])
result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
result += "\n\nWatermark : {}".format(data["result"]["watermark"])
result += "\n\nNo watermark : {}".format(data["result"]["no_watermark"])
print(result)
