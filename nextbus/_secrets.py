import os
import pandas as pd

class AppSecrets(object):
    def __init__(self, secret_file):
        if not os.path.isfile(secret_file):
            raise FileNotFoundError()

        self._secret_file = secret_file

        self.__load_secrets()

    def __load_secrets(self):
        secrets = pd.read_csv(self._secret_file, usecols=['name', 'value', 'encrypted'])
        # load all secrets
        self.__rtti_api_key = (secrets.loc[secrets['name'] == 'translink_api_key', 'value'].iloc[0])
        self.__google_api_client_id = (secrets.loc[secrets['name'] == 'translink_google_api_client_id', 'value'].iloc[0])
        self.__google_api_secret = (secrets.loc[secrets['name'] == 'translink_google_api_secret', 'value'].iloc[0])

    def get_rtti_api_key(self):
        return self.__rtti_api_key

    def get_google_api_client_id(self):
        return self.__google_api_client_id

    def get_google_api_secret(self):
        return self.__google_api_secret

# MY_SECRETS_CSV_FILE = '..\jtang-python-secrets.csv'

