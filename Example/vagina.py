from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.vagina()

# Get attributes
result = "Vagina Analyze"
result += "\nVagina : {}".format(data["result"]["vagina"])
result += "\nDepth : {}".format(data["result"]["depth"])
result += "\nGrip : {}".format(data["result"]["grip"])
result += "\nHumidity : {}".format(data["result"]["humidity"])
result += "\nElasticity : {}".format(data["result"]["elasticity"])
result += "\nDescription : {}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["picture"])
print(result)

# Get JSON results
print(data)
