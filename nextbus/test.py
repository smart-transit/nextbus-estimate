import os
from .appsecrets import AppSecrets

path = os.path.abspath(__file__)

print (os.path.dirname(path))

__root_path = os.path.dirname(os.path.abspath(__file__))

_MY_SECRETS_CSV_FILE = __root_path + r'\jtang-python-secrets.csv'

print(_MY_SECRETS_CSV_FILE)

secrets = AppSecrets(_MY_SECRETS_CSV_FILE)

import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))

print(json.loads(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3})))

