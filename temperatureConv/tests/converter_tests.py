from nose.tools import *
from converter.converter import Converter
import decimal


def converter_tests():
    test_conv = Converter()
    assert_equals(test_conv.tempConverter("c","k",10), decimal.Decimal('283.15'))
    assert_equals(test_conv.tempConverter("c","f",10), 50)
    assert_equals(test_conv.tempConverter("k","c",10), decimal.Decimal('-263.15'))
    assert_equals(test_conv.tempConverter("k","f",10), decimal.Decimal('-441.67'))
    assert_equals(test_conv.tempConverter("f","c",10), decimal.Decimal('-12.222'))
    assert_equals(test_conv.tempConverter("f","k",10), decimal.Decimal('260.93'))

#@raises(KeyError)
#def converter_raise_test():
#    test_raise = Converter()
#    assert_raises(KeyError,test_raise.tempConverter('z','a',10))
