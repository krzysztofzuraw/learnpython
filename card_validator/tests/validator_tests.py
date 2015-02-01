from nose.tools import *
import card_validator.validator as vali

#def test_return_dict():
    #assert_equals(vali.number_validator(123), {0:0, 1:2, 2:4, 3:6, 4:8, 5:1, 6:3, 7:5, 8:7, 9:9})

#def test_return_numbers():
    #assert_equals(vali.number_validator(1234789), [1, 2, 3, 4, 7, 8, 9])
    
#def test_even_numbers():
    #assert_equals(vali.number_validator(83423567), [3, 2, 5, 7])
    
#def test_even_values():
#    assert_equals(vali.number_validator(23567), [7, 3, 5, 6, 2])
#    assert_equals(vali.number_validator(353275011731396), [3,1,3,4,7,1,0,2,1,5,3,2,3,9,6])

#def test_sum():
#    assert_equals(vali.number_validator(353275011731396), 50)
    
def test_good():
    assert_equals(vali.number_validator(353275011731396), "number is correct")
    assert_equals(vali.number_validator(5555555555554444), "number is correct")
    assert_equals(vali.number_validator(4111111111111111), "number is correct")
    
def test_bad():
    assert_equals(vali.number_validator(353275321731396), "there is something wrong with this number")
    assert_equals(vali.number_validator(3351250001228658), "there is something wrong with this number")
    assert_equals(vali.number_validator(5102590100676565), "there is something wrong with this number")
    
def test_raises():
    assert_raises(vali.number_validator("this is string"))
