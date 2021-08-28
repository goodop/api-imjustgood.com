from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.twitterdl("https://twitter.com/rendytr_/status/1367319659741990912?s=20")
result = "Video URL : {}".format(data["result"]["videoUrl"])
print(result)
