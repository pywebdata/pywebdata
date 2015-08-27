from servicemanager import ServiceManager

def Service(name):
    if not ServiceManager.is_initialized:
        ServiceManager.load_all()
    return ServiceManager.fetch_service(name)

class ServiceGroup(object):

    def __init__(self, *args):
        self.services = args

    def link(self, param_name, *args):
        for arg in args:
            arg.set_alias(param_name)

    def query(self, qry=None, **kwargs):
        
        if isinstance(qry, dict):
            pass
        if isinstance(qry, str):
            pass
        if isinstance(qry, list):
            return map(self.query, qry)

        for service in self.services:
            service.query(qry, **kwargs)