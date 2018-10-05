
import pandas 
from translink import rttiapi
import pandas as pd


MY_SECRETS_CSV_FILE = '..\jtang-python-secrets.csv'

secrets = pd.read_csv(MY_SECRETS_CSV_FILE, usecols=['name', 'value', 'encrypted'])

# print(secrets)
apiKey = (secrets.loc[secrets['name'] == 'translink-api-key', 'value'].iloc[0])


api = rttiapi.RTTI(apiKey)
stop = api.stop('53095')
print(stop)

buses = api.buses('53095')
print (buses)

print ('stop.Name =' + stop.Name)
    #'WB DOVER ST FS ROYAL OAK AVE'
print ('WheelchairAccess = ' + stop.WheelchairAccess)
