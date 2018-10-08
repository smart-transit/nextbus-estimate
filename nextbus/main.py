
import pandas 
import _secrets
import googlemaps
from pprint import pprint
from translink import rttiapi

MY_SECRETS_CSV_FILE = '..\jtang-python-secrets.csv'

secrets = _secrets.AppSecrets(MY_SECRETS_CSV_FILE)

api = rttiapi.RTTI(secrets.get_rtti_api_key())
maps = googlemaps.Client(
        client_id= secrets.get_google_api_client_id,
        client_secret= secrets.get_google_api_secret)



stop = api.stop('53095')
#pprint(stop)

print ('Stop')
print ('\tNo = ' + str(stop.StopNo))
print ('\tName =' + stop.Name)
print ('\tRoute(s) =' + stop.Routes)
print ('\tgeo.location = ' + str(stop.Latitude) + ',' + str(stop.Longitude))
print ('\tWheelchairAccess = ' + str(stop.WheelchairAccess))

buses = api.buses('53095')
#print (buses)
for bus in buses:
    print ('Bus')
    print ('\tVehicle# = ' + bus.VehicleNo)
    print ('\tTripId = ' + str(bus.TripId)) 
    print ('\tRouteNo = ' + bus.RouteNo)
    print ('\tgeo.location = ' + str(bus.Latitude) + ',' + str(bus.Longitude))
    print ('\tDirection = ' + bus.Direction)
    print ('\tDestination = ' + bus.Destination)
    print ('\tLastUpdate = ' + str(bus.RecordedTime))
#print(stop.Name)

