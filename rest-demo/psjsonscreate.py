from json import dumps

keys = ['login', 'password', 'uid', 'gid', 'gecos', 'home', 'shell']
values = ['root', 'x', 0, 0, '', '/home/ravi', '/bin/bash']

print(dumps(dict(zip(keys, values)), indent=4))  # encode 
