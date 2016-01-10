from pywebdata.baseservice import BaseService

class Neighbourhood(BaseService):

    name = 'geonames-neighbourhood'

    def __init__(self):
        self.add_url('http://api.geonames.org/neighbourhoodJSON?lat=$latitude&lng=$longitude&username=demo')
        self.add_input('latitude', iotype='float', required=True, min=-90., max=90., incr=1.)
        self.add_input('longitude', iotype='float', required=True, min=-180., max=180., incr=1.)
        self.add_output('city', iotype='str')
        self.add_parser(staticmethod(lambda x:x['neighbourhood']))
