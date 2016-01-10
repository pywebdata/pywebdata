import baseexample as be

print 'Inputs:  ', be.elevation.get_input_names()
print 'Outputs: ', be.elevation.get_output_names()
print
print 'Example 1 : ', be.elevation.query(latitude=24, longitude=30)
print
print 'Example 2 : ', be.elevation.query({'latitude':24, 'longitude':30})
print
print 'Example 3 : ', be.elevation.query([{'latitude':24, 'longitude':30}, {'latitude':25, 'longitude':30}])
print
print 'Example 4 : ', be.elevation.query('latitude >= 24 and latitude <= 25 and longitude >= 30 and longitude < 31')
