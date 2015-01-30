from decimal import Decimal, getcontext

def pi_archimedes(n):
    """
    Calculate n iterations of Archimedes PI recurrence relation
    """
    polygon_egde_length_squared = Decimal(2)
    polygon_sides = 2
    for i in range(n):
        polygon_egde_length_squared = 2 - 2 * (1 - polygon_egde_length_squared / 4).sqrt()
        polygon_sides *= 2
    return polygon_sides * (polygon_egde_length_squared).sqrt()
    
def main():
    """
    Try the series
    """
    places = 100
    old_result = None
    for n in range(10 * places):
        # Calculations with double precision
        getcontext().prec = 2*places
        result = pi_archimedes(n)
        # Print the result with single precision
        getcontext().prec = places
        result = +result
        #import pdb
        #pdb.set_trace()
        print ("{0:<3d} : {1}".format(n,result))
        if result == old_result:
            break
        old_result = result
        
if __name__ == "__main__":
    main()
