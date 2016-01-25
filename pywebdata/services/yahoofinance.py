from pywebdata.baseservice import BaseService

class YahooFinance(BaseService):

    name = 'yahoo-finance'

    def __init__(self):
        self.add_url('http://finance.yahoo.com/webservice/v1/symbols/$listofsymbols/quote?format=json')
        self.add_input('listofsymbols', iotype='ListOfStrings', required=True, delimiter=',')
        self.add_output('symbol', iotype='str')
        self.add_output('name', iotype='str')
        self.add_output('price', iotype='float')
        self.add_output('volumne', iotype='int')
