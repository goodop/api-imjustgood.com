from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")

# GET STAMPLIST
# LINK https://api.imjustgood.com/stamplist
data    = api.stamplist()
result  = "STAMPLIST :"
for x in data:
    result += "\n{} ({})".format(data[x],x)
print(result)

# EXAMPLE GET CERTAIN ATTRIBUTES
image   = "https://i.ibb.co/vPJg8HG/example.jpg"
number  = "34"
data    = api.stamplist(number,image)
result  = "STAMP : {}".format(data["result"]["stamp"])
result += "URL : {}".format(data["result"]["image"])
print(result)
