from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.cctv_code()

# Get attributes
result += "CCTV Available"
for a in data["result"]["available"]:
    result += "\n{} {}".format(a,data["result"]["available"][a])
result += "\n\nCCTV Active"
for b in data["result"]["active"]:
    result += "\n{} {}".format(b,data["result"]["active"][b])
print(result)

# Get JSON results
print(data)
