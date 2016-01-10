import math
from itertools import ifilter

iotypes = {'float': float, 'int': int, 'str': str}

def frange(a, b=None, incr=1.):
  if b is None:
    b, a = a, 0.
  else:
    a = float(a)
  count = int(math.ceil(b - a)/incr)
  return (a + n*incr for n in range(count))

class Parameter(object):
    def __init__(self, iotype):
        self.iotype = iotypes[iotype]
        self.value = None

class Output(Parameter):
    def __init__(self, iotype, f_parse=None):
        Parameter.__init__(self, iotype)
        self.f_parse = f_parse

    def update(self, value):
        self.value = value

class Input(Parameter):

    def __init__(self, iotype, required=True, min=None, max=None, default=None, incr=None):
        Parameter.__init__(self, iotype)
        self.is_required = required
        self._min = min
        self._max = max
        self._default = default
        self._incr = incr
        self.valid = True

    def update(self, value):
        satisfy_min = not self._min or (self._min and value >= self._min)
        satisfy_max = not self._max or (self._max and value <= self._max)
        if satisfy_min and satisfy_max:
            self.value = value
            self.valid = True
        else:
            self.valid = False

    def set_incr(self, incr):
        self._incr = incr

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max

    def get_incr(self):
        return self._incr

    def get_range(self, condition_list):

        _min = self.get_min()
        _max = self.get_max()
        _incr = self.get_incr()

        whole_range = frange(_min, _max+_incr, _incr)

        def satisfy_all(val):

            def satisfy_one(cond):
                return cond['operator'](val, self.iotype(cond['value']))

            comps = map(satisfy_one, condition_list)

            return all(comps)

        return ifilter(satisfy_all, whole_range)
