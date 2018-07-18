content = """
{
    "login": "root",
    "password": "x",
    "uid": 0,
    "gid": 0,
    "gecos": "",
    "home": "/home/ravi",
    "shell": "/bin/bash"
}
"""
from json import loads
# decode
content = loads(content)
print(list(content.keys()))
print(list(content.values()))