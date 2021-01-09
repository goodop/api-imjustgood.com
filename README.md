#-- api.imjustgood.com
Sample request for api.imjustgood.com
please visit webpage imjustgood.com for more details.


## Example:
```python
from justgood import imjustgood

media = imjustgood("YOUR_APIKEY")

if text.startswith("cinema "):
    query = ' '.join(text.split()[1:]).lstrip().rstrip()
    data = media.cinema(query)
    print(data)
```
