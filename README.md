### Documentation
Full documentation available on https://api.imjustgood.com

### Installation
```python
pip install justgood
```

### Example
Here is how to use the module in your own python code. we choose <a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/instapost.py">instapost</a> media as an example.
```python
from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
post_url = "https://instagram.com/p/CJtqfEbhpjO/"
data = media.instapost(post_url)
print(data)
```

Response results
```json
{
    "creator": "ImJustGood", 
    "result": {
        "caption": "Get Started\napi.imjustgood.com\n.\n#imjustgood #tac #theautobotscorp", 
        "created": "2 days ago", 
        "fullname": "The Autobots Corporation", 
        "picture": "https://scontent-sin6-1.cdninstagram.com/v/t51.2885-19/s150x150/135785550_234471278085178_3734782670290828910_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_ohc=HQdOrvJcYNYAX-g_hAo&tp=1&oh=4780e9fa82b62dd71356498dfed7c362&oe=6022085E", 
        "postData": [
            {
                "postUrl": "https://scontent-sin6-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/135665982_715565716018895_1563117747618145065_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=111&_nc_ohc=A0n5IQVkjiAAX8VxJAr&tp=1&oh=427134cb92b3ce8ed9179dab92482ad2&oe=60232E2A", 
                "type": "image"
            },
            {
                "postUrl": "https://scontent-sin6-2.cdninstagram.com/v/t50.2886-16/136676648_446366420077083_6874742578521195210_n.mp4?_nc_ht=scontent-sin6-2.cdninstagram.com&_nc_cat=103&_nc_ohc=mEzo-awDsoYAX9wKFgP&oe=5FFBC9C2&oh=725ceccf6e4668be7b8a4be70afbd7aa", 
                "poster": "https://scontent-sin6-3.cdninstagram.com/v/t51.2885-15/e35/135519816_2504157059888884_6711864394916943089_n.jpg?_nc_ht=scontent-sin6-3.cdninstagram.com&_nc_cat=104&_nc_ohc=yy5oCKYuc-sAX9JgZjA&tp=1&oh=d0d48a6eb5275bf296eb8e05128a3882&oe=5FFB7530", 
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
Get Started
api.imjustgood.com
.
#imjustgood #tac #theautobotscorp

>>> picture = data["result"]["picture"]
>>> print(picture)
https://scontent-sin6-1.cdninstagram.com/v/t51.2885-19/s150x150/135785550_234471278085178_3734782670290828910_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_ohc=HQdOrvJcYNYAX-g_hAo&tp=1&oh=4780e9fa82b62dd71356498dfed7c362&oe=6022085E

>>> for a in data["result"]["postData"]:
...     print(a["postUrl"])
https://scontent-sin6-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/135665982_715565716018895_1563117747618145065_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=111&_nc_ohc=A0n5IQVkjiAAX8VxJAr&tp=1&oh=427134cb92b3ce8ed9179dab92482ad2&oe=60232E2A
https://scontent-sin6-2.cdninstagram.com/v/t50.2886-16/136676648_446366420077083_6874742578521195210_n.mp4?_nc_ht=scontent-sin6-2.cdninstagram.com&_nc_cat=103&_nc_ohc=mEzo-awDsoYAX9wKFgP&oe=5FFBC9C2&oh=725ceccf6e4668be7b8a4be70afbd7aa
```

### More Media Features
<table>
    <tbody>
        <tr>
            <td>Apikey Status</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/apikey_status.py">example</a></td>
        </tr>
        <tr>
            <td>Youtube Search</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/apikey_status.py">example</a></td>
        </tr>
        <tr>
            <td>Youtube Downloader</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/apikey_status.py">example</a></td>
        </tr>
    </tbody>
</table>
