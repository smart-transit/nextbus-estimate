import json
from pprint import pprint

distance_json ="""
 {"destination_addresses": ["Westbound Dover St @ Royal Oak Ave, Burnaby, BC V5H 1R4, Canada"],
                 "origin_addresses": ["58 Central Blvd, Burnaby, BC V5H 4M3, Canada"],
                 "rows": [{"elements": [{"distance": {"text": "2.4 km", "value": 2365},
                         "duration": {"text": "8 mins", "value": 481},
                         "duration_in_traffic": {"text": "7 mins",
                                                 "value": 405},
                         "status": "OK"}]}],
                "status": "OK"}
"""
 
data = json.loads(distance_json)

pprint (data)


pprint(data['rows'][0]['elements'][0]['distance'])
pprint(data['rows'][0]['elements'][0]['duration_in_traffic'])

pprint(data['rows'][0]['elements'][0]['distance']['value'])
pprint(data['rows'][0]['elements'][0]['duration_in_traffic']['value'])


class GoogleDistance(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(data)
        

    def get_duration_in_traffic(self):
        return self.__dict__['rows'][0]['elements'][0]['duration_in_traffic']['value']

    def get_distance(self):
        return self.__dict__['rows'][0]['elements'][0]['distance']['text']

distance = GoogleDistance(distance_json)
print(distance.destination_addresses)
print(distance.origin_addresses)
#print(distance.rows[0]['elements'][0]['duration_in_traffic']['value'])

print (distance.get_duration_in_traffic())
print (distance.get_distance())