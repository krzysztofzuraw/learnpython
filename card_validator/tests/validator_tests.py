from nose.tools import *
import card_validator.validator as vali

    
def test_good():
    assert_equals(vali.number_validator(353275011731396), "number is correct")
    assert_equals(vali.number_validator(4251250001228658), "number is correct")
    assert_equals(vali.number_validator(5102590100666565), "number is correct")
    
def test_bad():
    assert_equals(vali.number_validator(353275321731396), "there is something wrong with this number")
    assert_equals(vali.number_validator(3351250001228658), "there is something wrong with this number")
    assert_equals(vali.number_validator(5102590100676565), "there is something wrong with this number")
    
def test_raises():
    assert_raises(vali.number_validator("this is string"))
    
def test_issuer():
    assert_equals(vali.check_issuer(4251250001228658), "This is visa card")
    assert_equals(vali.check_issuer(5472273905057379), "This is mastercard card")
    assert_equals(vali.check_issuer(36170215240192), "This is diners card")
    assert_equals(vali.check_issuer(30023311669671), "This is diners card")
    assert_equals(vali.check_issuer(38820566293970), "This is diners card")
    assert_equals(vali.check_issuer(3158339997617473), "This is jcb card")
    assert_equals(vali.check_issuer(3088413936087240), "This is jcb card")
    assert_equals(vali.check_issuer(3528458724389371), "This is jcb card")
    assert_equals(vali.check_issuer(3337342018736425), "This is jcb card")
    assert_equals(vali.check_issuer(3402797694631333), "This is american express card")
    assert_equals(vali.check_issuer(3337342018), "This is not credit card number")
    
