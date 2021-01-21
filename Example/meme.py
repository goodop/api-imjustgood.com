from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")

text1 = "top" # example top text
text2 = "bottom" # example bottom text
imageUrl = "http://www.gstatic.com/webp/gallery/1.png" # example image url

data = media.meme(text1,text2,imageUrl)
result = data["result"]

print(result)
