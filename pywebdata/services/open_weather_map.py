from pywebdata.baseservice import BaseService

class OpenWeatherMap(BaseService):

    name = 'open-weather-map'

    def __init__(self):
        self.add_url('http://api.openweathermap.org/data/2.5/weather?q=$city&appid=2de143494c0b295cca9337e1e96b00e0')
        self.add_input('city', iotype='str', required=True)
        self.add_output('temp', iotype='float')
        self.add_parser(staticmethod(lambda x:x['main']))
