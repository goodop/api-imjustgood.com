from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.image("teacher")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result = "GOOGLE IMAGE RESULT :"
for i in range(len(data["result"])):
    result += f"\n{i+1}. {data['result'][i]}"
print(result)
