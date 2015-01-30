from nose.tools import *
import primeFactor.primefactor as calc

def prime_test():
    assert_equals(calc.calculate_prime_factor(600851475143), [71, 839, 1471, 6857])
    assert_equals(calc.calculate_prime_factor(1), [])
    assert_equals(calc.calculate_prime_factor(4), [2,2])
