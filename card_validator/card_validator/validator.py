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
    #if (10 - sum(number_list) % 10) % 10 == number_list[0]:
    #     return "ok"
    
#TODO: check bank name of card
    
