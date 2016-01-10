from pywebdata import Service
from pywebdata import Topology

lat = 40.78743
lon = -73.96625

elevation = Service('google-elevation-api')
neighbourhood = Service('geonames-neighbourhood')
weather = Service('open-weather-map')

topology = Topology()
topology.connect(neighbourhood, weather)

position = {'latitude': lat, 'longitude': lon}
topology.read_input(position)
topology.run()

print "Input:", position
print "Output:"
print neighbourhood.get_output_values()
print weather.get_output_values()
