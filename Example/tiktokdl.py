from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
url_post = "https://www.tiktok.com/@mamayukakuroyanagi/video/6810023518508518657" # example tiktok video url

data = media.tiktokdl(url_post)
video = data["result"]["videoUrl"]

print(video)
