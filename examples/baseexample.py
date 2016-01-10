import os, sys

here = os.path.dirname(__file__)
top = os.path.join(here, '..')
sys.path.insert(0, top)

from pywebdata import Service

elevation = Service('google-elevation-api')
neighbourhood = Service('geonames-neighbourhood')
weather = Service('open-weather-map')
