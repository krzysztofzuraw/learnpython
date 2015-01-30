from nose.tools import *
from Cezar.cezar_cipher import *

def test_enrypt_3():
    assert_equals(encrypt_3('A'), 'D')
    result = encrypt_3('abcdefghijklmnoprstuwxyz')
    assert_equals(result, 'DEFGHIJKLMNOPQRSUVWXZABC')
    assert_equals(encrypt_3('Ala ma kota'), 'DOD PD NRWD')
    assert_raises(ValueError, encrypt_3, '1')

def test_decrypt_3():
    assert_equals(decrypt_3('C'), 'Z')
    assert_equals(decrypt_3('DEFGHIJKLMNOPQRSUVWXZABC'), 'ABCDEFGHIJKLMNOPRSTUWXYZ')
    assert_equals(decrypt_3('FHCDU FLSKHU'), 'CEZAR CIPHER')
    assert_raises(ValueError, decrypt_3, "@")
    
def test_encrypt_13():
    assert_equals(encrypt_13('A'), 'N')
    assert_equals(encrypt_13('ABCDEFGHIJKLMNOPRSTUWXYZ'), 'NOPQRSTUVWXYZABCEFGHJKLM')
    assert_equals(encrypt_13('THIS IS ROT'), 'GUVF VF EBG')
    assert_raises(ValueError, encrypt_13, '78*((((*')
    
def test_decrypt_13():
    assert_equals(encrypt_13('N'), 'A')

