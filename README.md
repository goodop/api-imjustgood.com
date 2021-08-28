## API.IMJUSTGOOD.COM
```
█ █▀▄▀█   █ █ █ █▀ ▀█▀ █▀▀ █▀█ █▀█ █▀▄
█ █ ▀ █ █▄█ █▄█ ▄█  █  █▄█ █▄█ █▄█ █▄▀
api media service to make your code more better.
```
<p>
    <a href="http://pypi.org/project/justgood" rel="nofollow">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/justgood?label=PyPI" style="max-width:100%;">
    </a>
    <a href="https://github.com/RendyTR/api.imjustgood.com" rel="nofollow">
        <img alt="Update" src="https://img.shields.io/github/last-commit/rendytr/api.imjustgood.com?color=red&label=Update" height="20" style="max-width:100%;">
    </a>
    <a href="https://github.com/RendyTR" rel="nofollow">
        <img alt="Views" src="https://komarev.com/ghpvc/?username=RendyTR&color=green&label=Views" height="20" style="max-width:100%;">
    </a>
</p>

Full documentation available <a href="https://api.imjustgood.com/">here</a>

### Installation
```
pip3 install justgood
```

### Upgrade
```
pip3 install --upgrade justgood
```

### Example
Here is how to use the module in your own python code. we choose <a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/instapost.py">instapost</a> media as an example.
```python
from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.instapost("https://instagram.com/p/COjHqwGhFA6/")

print(data)
```

Response results
```json
{
    "creator": "ImJustGood", 
    "result": {
        "caption": "GET STARTED NOW\nhttps://api.imjustgood.com\n#autobots #rendytr #imjustgood", 
        "created": "2 weeks ago", 
        "fullname": "The Autobots Corporation", 
        "likes": "8",
        "picture": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/s150x150/156716508_792361228290684_2737571466878743960_n.jpg?tp=1&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_ohc=rpY8_az5H7gAX-ixW8W&edm=AP_V10EBAAAA&ccb=7-4&oh=660db30b81c81cf4eb6904c4937aa066&oe=60B73467&_nc_sid=4f375e", 
        "postData": [
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/182551939_1505660729785431_4872170436067358847_n.jpg?tp=1&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_ohc=4hwRibBJhRsAX-elcAw&edm=AP_V10EBAAAA&ccb=7-4&oh=d64890598377516a254a6d8bf5bdad41&oe=60B680F5&_nc_sid=4f375e", 
                "type": "image"
            }, 
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/182772702_212190447098888_3451476763231220039_n.jpg?tp=1&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=108&_nc_ohc=nacAdgapPioAX9oO99M&edm=AP_V10EBAAAA&ccb=7-4&oh=b605fbc309664405b8d1d936fe9b30ce&oe=60B6E2F7&_nc_sid=4f375e", 
                "type": "image"
            }, 
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t50.2886-16/183065958_515613456128123_180962327655226030_n.mp4?_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_ohc=HqRjnESsF-cAX8o4AeL&edm=AP_V10EBAAAA&ccb=7-4&oe=60B25D7F&oh=ce2f464d4ef43106620b6bf68f443b99&_nc_sid=4f375e", 
                "poster": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/e35/182468569_529144071448455_8659487135953051116_n.jpg?tp=1&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_ohc=UT35RAAdxOIAX8MGqk9&edm=AP_V10EBAAAA&ccb=7-4&oh=9370c6ee9c9a32123800ddb5492aa37d&oe=60B2A563&_nc_sid=4f375e", 
                "type": "video"
            }
        ], 
        "slidePost": true, 
        "username": "the.autobots_corp"
    }, 
    "status": 200
}
```

Get certain attributes
```
>>> username = data["result"]["username"]
>>> print(username)
the.autobots_corp

>>> fullname = data["result"]["fullname"]
>>> print(fullname)
The Autobots Corporation

>>> created = data["result"]["created"]
>>> print(created)
2 days ago

>>> caption = data["result"]["caption"]
>>> print(caption)
GET STARTED NOW
https://api.imjustgood.com
#autobots #rendytr #imjustgood

>>> picture = data["result"]["picture"]
>>> print(picture)
https://scontent-sin6-1.cdninstagram.com/v/t51.2885-19/s150x150/135785550_234471278085178_3734782670290828910_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_ohc=HQdOrvJcYNYAX-g_hAo&tp=1&oh=4780e9fa82b62dd71356498dfed7c362&oe=6022085E

>>> for a in data["result"]["postData"]:
...     print(a["postUrl"])
https://scontent-sin6-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/135665982_715565716018895_1563117747618145065_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=111&_nc_ohc=A0n5IQVkjiAAX8VxJAr&tp=1&oh=427134cb92b3ce8ed9179dab92482ad2&oe=60232E2A
https://scontent-sin6-2.cdninstagram.com/v/t50.2886-16/136676648_446366420077083_6874742578521195210_n.mp4?_nc_ht=scontent-sin6-2.cdninstagram.com&_nc_cat=103&_nc_ohc=mEzo-awDsoYAX9wKFgP&oe=5FFBC9C2&oh=725ceccf6e4668be7b8a4be70afbd7aa
```

### More Media Fitures
<table>
    <tbody>
        <tr>
            <td>Apikey Status</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/status.py">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/youtube.py">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/youtubedl.py">Example</a></td>
        </tr>
        <tr>
            <td>Joox Music</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/joox.py">Example</a></td>
        </tr>
        <tr>
            <td>Lyric Finder</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/lyric.py">Example</a></td>
        </tr>
        <tr>
            <td>Smule Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/smule.py">Example</a></td>
        </tr>
        <tr>
            <td>Smule Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/smuledl.py">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/tiktok.py">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/tiktokdl.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/instagram.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Post</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/instapost.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Story</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/instastory.py">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/twitter.py">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/twitterdl.py">Example</a></td>
        </tr>
        <tr>
            <td>Facebook Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/facebookdl.py">Example</a></td>
        </tr>
        <tr>
            <td>GitHub Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/github.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE Secondary</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/lineqr.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE Timeline</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/timeline.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE App Version</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/lineapp.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/search.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/image.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Playstore</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/playstore.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Translate</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/translate.py">Example</a></td>
        </tr>
        <tr>
            <td>Wallpaper HD</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/wallpaper.py">Example</a></td>
        </tr>
        <tr>
            <td>Porn Videos</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/porn.py">Example</a></td>
        </tr>
        <tr>
            <td>Pornstar</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/pornstar.py">Example</a></td>
        </tr>
        <tr>
            <td>Hentai</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/hentai.py">Example</a></td>
        </tr>
        <tr>
            <td>Kamasutra</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/kamasutra.py">Example</a></td>
        </tr>
        <tr>
            <td>Dick Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/dick.py">Example</a></td>
        </tr>
        <tr>
            <td>Tits Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/tits.py">Example</a></td>
        </tr>
        <tr>
            <td>Vagina Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/vagina.py">Example</a></td>
        </tr>
        <tr>
            <td>Meme Generator</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/meme.py">Example</a></td>
        </tr>
        <tr>
            <td>Movie Review</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/movie.py">Example</a></td>
        </tr>
        <tr>
            <td>Movie Quotes</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/movie_quotes.py">Example</a></td>
        </tr>
        <tr>
            <td>Cinema 21</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/cinema.py">Example</a></td>
        </tr>
        <tr>
            <td>TinyUrl</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/tinyurl.py">Example</a></td>
        </tr>
        <tr>
            <td>Bit.ly</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/bitly.py">Example</a></td>
        </tr>
        <tr>
            <td>KBBI</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/kbbi.py">Example</a></td>
        </tr>
        <tr>
            <td>Top News</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/topnews.py">Example</a></td>
        </tr>
        <tr>
            <td>Wikipedia</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/wikipedia.py">Example</a></td>
        </tr>
        <tr>
            <td>Urban Dictionary</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/urban.py">Example</a></td>
        </tr>
        <tr>
            <td>Zodiac Daily</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/zodiac.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Waktu Sholat</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/adzan.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Cuaca Dunia</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/cuaca.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Gempa BMKG</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/bmkg.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Corona Virus</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/corona.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Lowongan Kerja</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/karir.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Resi Pengiriman</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/resi.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Phone Cellular</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/cellular.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Lahir</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/lahir.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Jadian</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/jadian.py">Example</a></td>
        </tr>
        <tr>
            <td>Arti Nama</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/nama.py">Example</a></td>
        </tr>
        <tr>
            <td>Arti Mimpi</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/mimpi.py">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Sekarang</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/acaratv.py">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Stasiun</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/acaratv_channel.py">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Code</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/cctv_code.py">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/cctv_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Manga Search</td>
            <td>Deactive</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/manga_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Manga Chapter</td>
            <td>Deactive</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/manga_chapter.py">Example</a></td>
        </tr>
        <tr>
            <td>Calculator</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/calc.py">Example</a></td>
        </tr>
        <tr>
            <td>Languages Code</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/translate.py">Example</a></td>
        </tr>
        <tr>
            <td>Check IP Address</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/check_ip.py">Example</a></td>
        </tr>
        <tr>
            <td>Binary Encode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/BinaryEncode.py">Example</a></td>
        </tr>
        <tr>
            <td>Binary Decode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/BinaryDecode.py">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Encode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/B64Encode.py">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Decode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/B64Decode.py">Example</a></td>
        </tr>
        <tr>
            <td>Screenshot Web</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/screenshot.py">Example</a></td>
        </tr>
        <tr>
            <td>ASCII Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/ascii.py">Example</a></td>
        </tr>
        <tr>
            <td>Fancy Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/fancy.py">Example</a></td>
        </tr>
        <tr>
            <td>Customize URL</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/customlink.py">Example</a></td>
        </tr>
        <tr>
            <td>GIF Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/gif.py">Example</a></td>
        </tr>
        <tr>
            <td>Image to URL</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/imgurl.py">Example</a></td>
        </tr>
        <tr>
            <td>Text to Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/imagetext.py">Example</a></td>
        </tr>
        <tr>
            <td>Watermark Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/watermark_text.py">Example</a></td>
        </tr>
        <tr>
            <td>Watermark Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/watermark_image.py">Example</a></td>
        </tr>
        <tr>
            <td>SimiSimi</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/simisimi.py">Example</a></td>
        </tr>
    </tbody>
</table>

### Contact us
* <a href="https://imjustgood.com/team">Imjustgood Team</a>
* <a href="https://api.imjustgood.com/custom/forum">LINE Openchat</a>
