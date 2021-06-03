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

### Documentation
Full documentation available on https://api.imjustgood.com

### Installation
```
pip install justgood
```

### Upgrade
```
pip install --upgrade justgood
```

### Example
Here is how to use the module in your own python code. we choose <a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/instapost.py">instapost</a> media as an example.
```python
from justgood import imjustgood

api = imjustgood("Your_Apikey_Here")
url = "https://instagram.com/p/COjHqwGhFA6/"
data = api.instapost(url)

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
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/cc4234a2c12893c965932a37799f6d1dc49122d3/example.py#L13">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L23">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L35">Example</a></td>
        </tr>
        <tr>
            <td>Joox Music</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L47">Example</a></td>
        </tr>
        <tr>
            <td>Lyric Finder</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L57">Example</a></td>
        </tr>
        <tr>
            <td>Smule Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L64">Example</a></td>
        </tr>
        <tr>
            <td>Smule Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L106">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L117">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L134">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L141">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Post</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L168">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Story</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L187">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L204">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L216">Example</a></td>
        </tr>
        <tr>
            <td>Facebook Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L221">Example</a></td>
        </tr>
        <tr>
            <td>GitHub Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L228">Example</a></td>
        </tr>
        <tr>
            <td>LINE Secondary</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L248">Example</a></td>
        </tr>
        <tr>
            <td>LINE Timeline</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L284">Example</a></td>
        </tr>
        <tr>
            <td>LINE App Version</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L303">Example</a></td>
        </tr>
        <tr>
            <td>Google Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L310">Example</a></td>
        </tr>
        <tr>
            <td>Google Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L320">Example</a></td>
        </tr>
        <tr>
            <td>Google Playstore</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L326">Example</a></td>
        </tr>
        <tr>
            <td>Google Translate</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L338">Example</a></td>
        </tr>
        <tr>
            <td>Wallpaper HD</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L352">Example</a></td>
        </tr>
        <tr>
            <td>Porn Videos</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L358">Example</a></td>
        </tr>
        <tr>
            <td>Pornstar</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L368">Example</a></td>
        </tr>
        <tr>
            <td>Hentai</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L384">Example</a></td>
        </tr>
        <tr>
            <td>Kamasutra</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L389">Example</a></td>
        </tr>
        <tr>
            <td>Dick Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L396">Example</a></td>
        </tr>
        <tr>
            <td>Tits Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L417">Example</a></td>
        </tr>
        <tr>
            <td>Vagina Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L406">Example</a></td>
        </tr>
        <tr>
            <td>Meme Generator</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L427">Example</a></td>
        </tr>
        <tr>
            <td>Movie Review</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L435">Example</a></td>
        </tr>
        <tr>
            <td>Movie Quotes</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L451">Example</a></td>
        </tr>
        <tr>
            <td>Cinema 21</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L456">Example</a></td>
        </tr>
        <tr>
            <td>TinyUrl</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L506">Example</a></td>
        </tr>
        <tr>
            <td>Bit.ly</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L511">Example</a></td>
        </tr>
        <tr>
            <td>KBBI</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L521">Example</a></td>
        </tr>
        <tr>
            <td>Top News</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L526">Example</a></td>
        </tr>
        <tr>
            <td>Wikipedia</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L538">Example</a></td>
        </tr>
        <tr>
            <td>Urban Dictionary</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L544">Example</a></td>
        </tr>
        <tr>
            <td>Zodiac Daily</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L551">Example</a></td>
        </tr>
        <tr>
            <td>Info Waktu Sholat</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L566">Example</a></td>
        </tr>
        <tr>
            <td>Info Cuaca Dunia</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L581">Example</a></td>
        </tr>
        <tr>
            <td>Info Gempa BMKG</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L590">Example</a></td>
        </tr>
        <tr>
            <td>Info Corona Virus</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L605">Example</a></td>
        </tr>
        <tr>
            <td>Info Lowongan Kerja</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L619">Example</a></td>
        </tr>
        <tr>
            <td>Info Resi Pengiriman</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L638">Example</a></td>
        </tr>
        <tr>
            <td>Info Phone Cellular</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L659">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Lahir</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L676">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Jadian</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L685">Example</a></td>
        </tr>
        <tr>
            <td>Arti Nama</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L692">Example</a></td>
        </tr>
        <tr>
            <td>Arti Mimpi</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L699">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Sekarang</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L707">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Stasiun</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L717">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Code</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L724">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L734">Example</a></td>
        </tr>
        <tr>
            <td>Manga Search</td>
            <td>Maintenance</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L744">Example</a></td>
        </tr>
        <tr>
            <td>Manga Chapter</td>
            <td>Maintenance</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L758">Example</a></td>
        </tr>
        <tr>
            <td>Calculator</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L804">Example</a></td>
        </tr>
        <tr>
            <td>Languages Code</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L345">Example</a></td>
        </tr>
        <tr>
            <td>Check IP Address</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L809">Example</a></td>
        </tr>
        <tr>
            <td>Binary Encode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L821">Example</a></td>
        </tr>
        <tr>
            <td>Binary Decode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L826">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Encode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L831">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Decode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L836">Example</a></td>
        </tr>
        <tr>
            <td>Screenshot Web</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L767">Example</a></td>
        </tr>
        <tr>
            <td>ASCII Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L841">Example</a></td>
        </tr>
        <tr>
            <td>Fancy Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L845">Example</a></td>
        </tr>
        <tr>
            <td>Customize URL</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L516">Example</a></td>
        </tr>
        <tr>
            <td>GIF Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L774">Example</a></td>
        </tr>
        <tr>
            <td>Image to URL</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L779">Example</a></td>
        </tr>
        <tr>
            <td>Text to Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L784">Example</a></td>
        </tr>
        <tr>
            <td>Watermark Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L789">Example</a></td>
        </tr>
        <tr>
            <td>Watermark Icon</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L794">Example</a></td>
        </tr>
        <tr>
            <td>SimiSimi</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/a655bd89218a1f25747573aaed2572eadea1e461/example.py#L799">Example</a></td>
        </tr>
    </tbody>
</table>

### Contact us here
* <a href="https://imjustgood.com/team">Imjustgood Team</a>
* <a href="https://api.imjustgood.com/custom/forum">LINE Openchat Room</a>
