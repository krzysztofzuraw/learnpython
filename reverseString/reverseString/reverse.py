def reverse_string(string):
    return string[::-1]
        
def reverse_number(num):
    try:
        return float(str(num)[::-1])
    except ValueError:
        return "Please provide number"
        
