from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.hentai()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result = "HENTAI RESULT :"
for i in range(len(data["result"])):
    result += f"\n{i+1}. {data['result'][i]}"
print(result)
