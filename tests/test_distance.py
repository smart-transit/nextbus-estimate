import pprint
import googlemaps
from datetime import datetime

 gmaps = googlemaps.Client(key='<your_key>')

# Geocoding an address
#geocode_result_from = gmaps.geocode('10153 King George Hwy, Surrey, BC')
#geocode_result_to = gmaps.geocode('Surrey Memorial Hospital, 13750 96 Ave, Surrey, BC V3V 1Z2')

#pprint.pprint (geocode_result_from[0])
#pprint.pprint (geocode_result_from[0]['geometry']['location'])
#pprint.pprint (geocode_result_to[0]['geometry']['location'])

qry_origins = []
qry_dests = []
qry_origins.append({'lat': 49.1864648, 'lng': -122.848401})
qry_dests.append({'lat': 49.1759547, 'lng': -122.8413971})
#qry_origins.append(geocode_result_to[0]['geometry']['location'])
#qry_dests.append(geocode_result_to[0]['geometry']['location'])

#print(qry_origins)
#print(qry_dests)

now = datetime.now()
# travel info between 2 geo locations
distance_result = gmaps.distance_matrix(origins = qry_origins, 
        destinations = qry_dests,
        mode = 'driving',
        departure_time=now)

pprint.pprint (distance_result)

# print (geocode_result)

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

#print (reverse_geocode_result)

# Request directions via public transit

# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
