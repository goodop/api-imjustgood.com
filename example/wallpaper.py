from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.wallpaper("nude")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
resut = "WALLPAPER RESULT :"
for i in range(len(data["result"])):
    result += f"\n{i+1}. {data['result'][i]}"
print(result)
