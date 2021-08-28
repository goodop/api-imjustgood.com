from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.acaratv_channel("globaltv")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result = "Jadwal Acara TV"
for a in data["result"]:
    result += "\n{}".format(a)
print(result)
