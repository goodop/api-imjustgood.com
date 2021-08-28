from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.fancy("IMJUSTGOOD")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result = "FANCY RESULT :\n"
for s in data["result"]:
    result += "\n{}\n".format(s)
print(result)
