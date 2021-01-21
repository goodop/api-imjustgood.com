from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
lang = "en" # example coutry code
text = "mengagumkan" # example text
data = media.translate(lang,text)
result = "{}".format(data["result"]["translate"])
print(result)

# more country code here >> https://api.imjustgood.com/language/code
