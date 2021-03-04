from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "komputer" # example your query search
data = media.kbbi(query)
result = data["result"]["desc"]

print(result)
