from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.twitterdl("https://twitter.com/rendytr_/status/1367319659741990912?s=20")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Caption : {}".format(data["result"]["caption"])
result += "\nLike : {}".format(data["result"]["likes"])
result += "\nRetweet : {}".format(data["result"]["retweet"])
if data["result"]["imageUrl"] != []:
    result += "\n\nImage URL : "
    for a in data["result"]["imageUrl"]:
        result += "\n{}".format(a)
if data["result"]["videoUrl"] != None:
    result += "\n\nVideo URL :\n{}".format(data["result"]["videoUrl"])
print(result)
