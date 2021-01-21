from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
sign = "aries" # example zodiac sign
data = media.zodiac(sign)

# Get attributes
result = "Zodiac Daily"
result += "\nSign : {}".format(data["result"]["zodiac"])
result += "\nCouple : {}".format(data["result"]["couple"])
result += "\nDate Range : {}".format(data["result"]["date"])
result += "\nLucky Color : {}".format(data["result"]["color"])
result += "\nLucky Time : {}".format(data["result"]["time"])
result += "\nLucky Number : {}".format(data["result"]["number"])
result += "\n\nPublic : {}".format(data["result"]["public"])
result += "\n\nMoney : {}".format(data["result"]["money"])
result += "\n\nLove Couple : {}".format(data["result"]["love"]["couple"])
result += "\n\nLove Single : {}".format(data["result"]["love"]["single"])
result += "\n\nImage : {}".format(data["result"]["image"])
print(result)

# Get JSON results
print(data)
