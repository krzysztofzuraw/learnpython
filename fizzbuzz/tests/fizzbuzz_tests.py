from nose.tools import *
from FizzBuzz.fizzbuzz import *

def fizz_test():
    assert_equal(fizz_buzz(3),'Fizz')
    assert_equal(fizz_buzz(15),'FizzBuzz')


