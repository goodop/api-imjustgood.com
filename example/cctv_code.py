from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.cctv_code()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result += "DAFTAR CCTV"
for a in data["result"]["available"]:
    result += "\n{} {}".format(a,data["result"]["available"][a])
result += "\n\nCCTV AKTIF"
for b in data["result"]["active"]:
    result += "\n{} {}".format(b,data["result"]["active"][b])
print(result)
