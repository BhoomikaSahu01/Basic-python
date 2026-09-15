'''Two types of modules in python:
- Build in Modules
- External Modules
https://docs.python.org/3/py-modindex.html
search google build in modules in python'''


import math
import os #os colous is ligh because we din't use it
import mymodule
import requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https: //www.google.com")
print(r.text)