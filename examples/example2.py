import baseexample as be

from pywebdata import Topology

lat = 40.78743
lon = -73.96625

topology = Topology()
topology.connect(be.neighbourhood, be.weather)

position = {'latitude': lat, 'longitude': lon}
topology.read_input(position)
topology.run()

print "Input:", position
print "Output:"
print be.neighbourhood.get_output_values()
print be.weather.get_output_values()
