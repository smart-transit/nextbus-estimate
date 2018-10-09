import os
from .appsecrets import AppSecrets

__root_path = os.path.dirname(os.path.abspath(__file__))

_MY_SECRETS_CSV_FILE = __root_path + r'\..\..\jtang-python-secrets.csv'
