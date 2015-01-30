import math
from decimal import Decimal, localcontext

def e_lim(n):
    """
    Calculate iterations of e using Newton Series Expansion
    :param int n: number of iteration
    :return e: base of natural logarithm 
    :rtype: decimal
    """
    #return (Decimal(1) + Decimal(1)/Decimal(n)) ** Decimal(n)  too much iteration (over 10k)
    #return (Decimal(1) + Decimal(n)) ** (Decimal(1) / Decimal(n))  good but for very small n
    return  Decimal(1)/Decimal(math.factorial(n))
    
def main(): 
    """
    Just for try
    """
    result = Decimal(0)
    places = 100
    old_result = None
    for i in range(16):
        with localcontext() as ctx:
            ctx.prec = 2 * places
            step = e_lim(i)
        result += step
        error = result - Decimal(math.e)
        print ("{0} : {1:.9f} with {2:.9f} err".format(i, result, error))
        if result == old_result:
            break
        old_result = result
    
    
if __name__ == "__main__":
    main()
        
        
        
