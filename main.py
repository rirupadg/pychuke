import urllib.request

with urllib.request.urlopen('https://docs.python.org/3/library/urllib.request.html#module-urllib.request') as f:

    print(f.read())
