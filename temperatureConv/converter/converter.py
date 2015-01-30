import decimal 
decimal.getcontext().prec = 5


class Converter(object):
    """ Converting between: Celcius, Kalvin and Farenheit"""
    _const = {'ck': lambda c: c + decimal.Decimal(273.15),
              'cf': lambda c: c*decimal.Decimal((9.0/5.0)) + decimal.Decimal(32),
              'kc': lambda k: k - decimal.Decimal(273.15),
              'kf': lambda k: k*decimal.Decimal(1.8) - decimal.Decimal(459.67),
              'fc': lambda f: (f-32)*decimal.Decimal(5.0/9.0),
              'fk': lambda f: (f+decimal.Decimal(459.67))*decimal.Decimal(5.0/9.0),
             }
    
    @classmethod
    def tempConverter(cls, from_units, to_units, value):
        """ @from_units: units to convert from
            @to_units: units to convert to
            @value: how much do you want to convert"""
        try:
            return cls._const[from_units[0]+to_units[0]](value)
        except KeyError:
            return "Can't convert from {0} to {1}".format(from_units, to_units)                
