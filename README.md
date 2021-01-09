## Documentation
Full documentation is available at http://api.imjustgood.com

## Example:
Here is how to use the module in your own python code
and i chose cinema 21 for example.

```python
from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")

if text.startswith("cinema "):
    query = text.split()[1]
    data = media.cinema(query)
    print(data)
```
