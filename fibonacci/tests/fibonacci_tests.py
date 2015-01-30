from nose.tools import *
from Fibonacci.fibonacci import *

def test_fibonacci():
    assert_equals(generate_fibonacci(5), [0,1,1,2,3,5])
    assert_equals(generate_fibonacci(0), [0])
    assert_equals(generate_fibonacci(1), [0,1])
    assert_equals(generate_fibonacci(2), [0,1,1])
