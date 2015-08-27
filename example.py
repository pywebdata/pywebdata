from pywebdata import Service, ServiceGroup

elev = Service('google-elevation-api')

print 'Inputs:  ', elev.get_input_names()
print 'Outputs: ', elev.get_output_names()
print
print 'Example 1 : ', elev.query(latitude=24, longitude=30)
print
print 'Example 2 : ', elev.query({'latitude':24, 'longitude':30})
print
print 'Example 3 : ', elev.query([{'latitude':24, 'longitude':30}, {'latitude':25, 'longitude':30}])
print
print 'Example 4 : ', elev.query('latitude >= 24 and latitude <= 25 and longitude >= 30 and longitude < 31')
