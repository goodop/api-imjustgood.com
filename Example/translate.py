from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
lang = "en" # example country code , more country code here >> https://api.imjustgood.com/language/code
text = "mengagumkan" # example text
data = media.translate(lang,text)

# Get attributes
result = data["result"]["translate"]
print(result)

# Get JSON results
print(data)
