from json import dump, dumps
from csv import reader


def csv2json(csv_file, json_file):
    keys = ['login', 'password', 'uid', 'gid', 'gecos', 'home', 'shell']

    payload = [dict(zip(keys, row)) for row in reader(open(csv_file), delimiter=':')]  # list comp.
    # print(payload)
    dump(payload, open(json_file, 'w'), indent=4)

    return dumps(payload, indent=4)


json_content = csv2json('passwd', 'passwd.json')
print(json_content)


# github.com/ravijaya/datafiles
