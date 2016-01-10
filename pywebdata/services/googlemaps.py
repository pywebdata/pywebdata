from pywebdata.baseservice import BaseService

class GoogleElevationAPI(BaseService):

    name = 'google-elevation-api'

    def __init__(self):
        self.add_url('http://maps.googleapis.com/maps/api/elevation/json?locations=$latitude,$longitude')
        self.add_input('latitude', iotype='float', required=True, min=-90., max=90., incr=1.)
        self.add_input('longitude', iotype='float', required=True, min=-180., max=180., incr=1.)
        self.add_output('elevation', iotype='float')
        self.add_parser(staticmethod(lambda x:x['results']))
