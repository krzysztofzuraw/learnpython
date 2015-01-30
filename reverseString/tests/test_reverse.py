from nose.tools import *
from reverseString import reverse

def test_reverse_string():
    result = reverse.reverse_string("one")
    assert_equal(result, "eno")
    assert_equal(reverse.reverse_string(['1', '2', '3']), ['3', '2', '1'])
    
def test_reverse_number():
    result = reverse.reverse_number(123)
    assert_equal(result, 321)
    assert_equal(reverse.reverse_number(456.789), 987.654)
