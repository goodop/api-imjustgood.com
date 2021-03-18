from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
url = "https://www.tiktok.com/@mamayukakuroyanagi/video/6810023518508518657" # example tiktok post url
data = media.tiktokdl(url)

# Get attributes
result = "TikTok Downloader"
result += "\nWatermark : {}".format(data["result"]["watermark"])
result += "\nNo watermark : {}".format(data["result"]["no_watermark"])
print(result)

# Get JSON results
print(data)
