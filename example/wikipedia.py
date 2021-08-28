from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.wikipedia("jakarta")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Wikipedia : {}".format(query)
result += "\nDescription : {}".format(data["result"])
print(result)
