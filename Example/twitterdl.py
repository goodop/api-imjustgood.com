from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
url = "https://twitter.com/rendytr_/status/1367319659741990912?s=20" # example tweet post url
data = media.twitterdl(url)
result = data["result"]["videoUrl"]

print(result)
