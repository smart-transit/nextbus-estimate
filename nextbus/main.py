import os
import sys
import pandas 
import googlemaps
from datetime import datetime
from appsecrets import AppSecrets
from pprint import pprint
from translink import rttiapi

import json
class DistanceMatrixResponse(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(data)

    def get_duration_in_traffic(self):
        return self.__dict__['rows'][0]['elements'][0]['duration_in_traffic']['text']

    def get_duration_in_traffic_in_seconds(self):
        return int(self.__dict__['rows'][0]['elements'][0]['duration_in_traffic']['value'])

    def get_distance(self):
        return self.__dict__['rows'][0]['elements'][0]['distance']['text']
    
    def get_distance_in_meter(self):
        return int(self.__dict__['rows'][0]['elements'][0]['distance']['value'])

    def get_origin_location(self):
        return self.origin_addresses[0]
        


def main():

    '''
        inital entry point of nextbus. A stop nuber and line number must be
        specified
    '''

    if len(sys.argv) != 3:
        print('sys.argv = ' + str(len(sys.argv)))
        print('A stop nuber and line(route) number must be specified')
        return
    
    _stopNo = sys.argv[1]
    _routeNo = sys.argv[2]

    # start getting stop and bus schedule/estimate 
    start(_stopNo, _routeNo)

def start(stopNo, routeNo):
    ''' 

    '''
    print('stop_no: ' +str(stopNo), 'routne_no: '+str(routeNo))
    #MY_SECRETS_CSV_FILE = '..\jtang-python-secrets.csv'
    secrets = AppSecrets(os.path.dirname(os.path.abspath(__file__)) + r'\..\..\jtang-python-secrets.csv')

    api = rttiapi.RTTI(secrets.get_rtti_api_key())
    gmaps = googlemaps.Client(
            client_id= secrets.get_google_api_client_id(),
            client_secret= secrets.get_google_api_secret())
    qry_origins = []
    qry_dests = []

    stop = api.stop(stopNo)
    #pprint(stop)

    print ('Stop')
    print ('\tNo = ' + str(stop.StopNo))
    print ('\tName =' + stop.Name)
    print ('\tRoute(s) =' + stop.Routes)
    print ('\tgeo.location = ' + str(stop.Latitude) + ',' + str(stop.Longitude))
    print ('\tWheelchairAccess = ' + str(stop.WheelchairAccess))

    qry_dests.append({'lat': stop.Latitude, 'lng': stop.Longitude})

    buses = api.buses(stopNo, routeNo)

    #print (buses)
    for bus in buses:
        
        qry_origins.append({'lat': bus.Latitude, 'lng': bus.Longitude})
        print ('Bus')
        print ('\tVehicle# = ' + bus.VehicleNo)
        print ('\tTripId = ' + str(bus.TripId)) 
        print ('\tRouteNo = ' + bus.RouteNo)
        print ('\tgeo.location = ' + str(bus.Latitude) + ',' + str(bus.Longitude))
        print ('\tDirection = ' + bus.Direction)
        print ('\tDestination = ' + bus.Destination)
        print ('\tLastUpdate = ' + str(bus.RecordedTime))

        #print (qry_origins)
        #print (qry_dests)
        now = datetime.now()
        # travel info between 2 geo locations
        distance_result = gmaps.distance_matrix(origins = qry_origins, 
                destinations = qry_dests,
                mode = 'driving',
                departure_time=now)

        #pprint(distance_result)

        obj = DistanceMatrixResponse(json.dumps(distance_result))

        print ('\tAway = ' + obj.get_distance())
        print ('\tArrives at = ' + obj.get_duration_in_traffic())
        print ('\tAt speed = {0} km/h'.format(round((obj.get_distance_in_meter() / 1000 / obj.get_duration_in_traffic_in_seconds() * 3600),1)))

        #pprint (distance_result)
        print ('\tBus.Location = ' + obj.get_origin_location())
        qry_origins.clear()

    
if __name__ == '__main__':
    main()
