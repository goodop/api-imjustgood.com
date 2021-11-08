from justgood import imjustgood

api      = imjustgood("YOUR_APIKEY_HERE")

# GET LIST QUR'AN SURAH
# LINK https://api.imjustgood.com/alquran=list
data     = api.alquran()
result   = "QUR'AN SURAH :"
for qs in data:
    result += "\n{}".format(qs)
print(result)

# EXAMPLE GET QUR'AN SURAH
data     = api.alquranQS("al-ikhlas")
audioUrl = data["result"]["audio"]
number   = data["result"]["number"]
total    = data["result"]["verse"]
meaning  = data["result"]["meaning"]
arab     = data["result"]["title"]["ar"]
latin    = data["result"]["title"]["id"]
place    = data["result"]["place"]
desc     = data["result"]["desc"]
verse    = data["result"]["verses"]
result   = "[QS:{}][{}]\n".format(number,total)
result  += "\n{}".format(arab)
result  += "\n{} ( {} )\n".format(latin,meaning)
for i in range(len(verse)):
    result += "\n{}".format(verse[i]["ar"])
    result += "\n{}. {}\n".format(i+1,verse[i]["id"])
result  += "\nDiturunkan di : {}\n".format(place)
result  += "\n{}".format(desc)
print(result)
print(audioUrl)
