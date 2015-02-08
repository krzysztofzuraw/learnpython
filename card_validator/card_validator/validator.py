import re

def number_validator(number):
    """
    Credit card validator using LUHN algorithm
    """
    table = {0:0, 1:2, 2:4, 3:6, 4:8, 5:1, 6:3, 7:5, 8:7, 9:9}
    try:
        number_list = list(reversed([int(x) for x in str(number)]))
    except ValueError:
        return "this is not a number, try again"
    for i,val in enumerate(number_list):
        if i % 2 == 1:
            if val in table.keys():
                number_list[i] = table.get(val)
    
    if sum(number_list) % 10 == 0:
        return "number is correct"
    else:
        return "there is something wrong with this number"
    

def check_issuer(number):
    """
    Check name of cards bank by  first digits
    """
    if len(str(number)) not in (14,16,17,18,19):
        return "This is not credit card number"
    visa = re.search('^4[\d]+', str(number))
    mastercard = re.search('^5[1-5][\d]+', str(number))
    diners = re.search('^2014[0-9]+|^2149[0-9]+|^30[0-5][0-9]+|^36[0-9]+|^38[0-9]+', str(number))
    jcb = re.search('^3[^4,6,7,8][0-9]+|^1800[0-9]+|^2131[0-9]+', str(number))
    express = re.search('^34[0-9]+|^36[0-9]+', str(number))
    if visa:
        return "This is visa card"
    elif mastercard:
        return "This is mastercard card"
    elif diners:
        return "This is diners card"
    elif jcb:
        return "This is jcb card"
    elif express:
        return "This is american express card"
    else:
        return "This issuer is not in database"
        
        
        
        
