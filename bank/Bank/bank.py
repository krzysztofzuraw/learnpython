import numbers
from abc import ABCMeta

class Account(object):
    __metaclass__ = ABCMeta
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0
        self.number = numbers.random_numbers(10)
        self.pin = numbers.random_numbers(4)
        #self.number = 1234 for testing
        #self.pin = 1111
        
    can_withdraw = True
             
class CheckingAccount(Account):
    pass                
class SavingsAccount(Account):
    can_withdraw = False        
class BuisnessAccount(Account):
    pass
        
def account_info(object):
    return "This is {0} account. It has {1} number, {2} balance and {3} pin" \
            .format(object.owner_name, object.number, object.balance, object.pin)
            
def atm(object, mode, amount, password):
    if mode == 'in':
        if password == object.pin:
            object.balance += amount
        else:
            return "Wrong pin, try again"
    elif mode == 'out' and object.can_withdraw:
        if password == object.pin:
            if amount <= object.balance:
                object.balance -= amount
            else:
                return "Your don't have cash in your account"
        else:
            return "Wrong pin"
    else:
        return "Please choose either in or out mode. Or you have savings account wich don't allow withdraw"

         
