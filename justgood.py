import json, requests, threading

class imjustgood(threading.Thread):
    def __init__(self, apikey):
        super(imjustgood, self).__init__()
        self.host = "https://api.imjustgood.com"
        self.headers = {"apikey": apikey}
        self.session = requests.Session()

    def PrintJson(self, jhon):
        print(json.dumps(jhon, indent=4, sort_keys=True))

    def Get(self, data, headers=None):
        if headers:
            headers = {**headers, **self.headers}
        else:
            headers = self.headers
        try:  
            req = json.loads(self.session.get(self.host+data,headers=headers).text)
        except:
            raise Exception("Under Maintenance.")
        if req["status"] != 200:
            raise Exception(str(req))
        return req

    def Post(self, path, headers=None, data=None, files=None, jhon=None):
        if headers:
            headers = {**headers, **self.headers}
        else:
            headers = self.headers
        try:
            req = json.loads(self.session.post(self.host+path,headers=headers,data=data,files=files,json=jhon).text)
        except:
            raise Exception("Under Maintenance.")
        if req["status"] != 200:
            raise Exception(str(req))
        return req

    def cinema(self, city):
        return self.Get("/cinema="+city)

    def youtube(self, query):
        return self.Get("/youtube="+query)

    def youtubedl(self, url):
        return self.Get("/youtubedl="+url)

    def twitter(self, userID):
        return self.Get("/twitter="+userID)

    def zodiac(self, sign):
        return self.Get("/zodiac="+sign)

    def image(self, query):
        return self.Get("/image="+query)

    def nama(self, name):
        return self.Get("/nama="+name)

    def mimpi(self, query):
        return self.Get("/mimpi="+query)

    def wallpaper(self, query):
        return self.Get("/wallpaper="+query)

    def tinyurl(self, url):
        return self.Get("/tinyurl="+url)

    def bitly(self, url):
        return self.Get("/bitly="+url)

    def porn(self, query):
        return self.Get("/porn="+query)

    def pornstar(self):
        return self.Get("/pornstar")

    def hentai(self):
        return self.Get("/hentai")

    def topnews(self):
        return self.Get("/topnews")

    def corona(self):
        return self.Get("/corona")

    def calc(self, digit):
        return self.Get("/calc="+digit)

    def wikipedia(self, query):
        return self.Get("/wikipedia="+query)

    def urban(self, query):
        return self.Get("/urban="+query)

    def movie(self, title):
        return self.Get("/movie="+title)

    def github(self, userID):
        return self.Get("/github="+userID)


############# S E M P L E #################
# from justgood import imjustgood
# juh = imjustgood("YOUR_APIKEY")
# yosgood = juh.cinema("jakarta")
# print(yosgood)