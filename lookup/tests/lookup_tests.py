from nose.tools import *
import Lookup.lookup as look

def ip_lookup_test():
    assert_equals(look.ip_lookup('89.68.110.222'), {'ip': '89.68.110.222', 'country': 'PL', 'host name': 'UPC-PL'} )
    assert_raises(look.ip_lookup('www'))
    
def www_lookup_test():
    assert_equals(look.www_lookup('www.onet.pl'), {'ip': '213.180.141.140', 'country': 'PL', 'host name': 'ONET-PL'})
    assert_equals(look.www_lookup('www.google.pl'), '')
