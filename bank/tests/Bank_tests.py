from nose.tools import *
from Bank.bank import *

def test_checking_account():
    checking = CheckingAccount('Adam')
    assert_equals(account_info(checking), "This is Adam account. It has 1234 number, 0 balance and 1111 pin")
    assert_equals(atm(checking, 'in', 100, 1111), None)
    assert_equals(atm(checking, 'in', 100, 1234), "Wrong pin, try again")
    assert_equals(atm(checking, 'zz', 123, 1111), "Please choose either in or out mode. Or you have savings account wich don't allow withdraw")
    assert_equals(atm(checking, 'out', 50, 1111), None)
    assert_equals(account_info(checking), "This is Adam account. It has 1234 number, 50 balance and 1111 pin")
    assert_equals(atm(checking, 'out', 150, 1111), "Your don't have cash in your account")
    
def test_savings_account():
    savings = SavingsAccount('Josh')
    assert_equals(atm(savings, 'in', 100, 1111), None)
    assert_equals(account_info(savings), "This is Josh account. It has 1234 number, 100 balance and 1111 pin")
    assert_equals(atm(savings, 'out', 100, 1111), "Please choose either in or out mode. Or you have savings account wich don't allow withdraw")
    
    

#def test_buisness_account():
#    buisness = BuisnessAccount('John')
#    assert_equals(account_info(buisness), "This is John account. It has 1234 number, 0 balance and 1111 pin")
#    assert_equals(buisness.atm_out(1334), None)
