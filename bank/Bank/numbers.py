from random import randrange

def random_numbers(n):
    """ Generate n digit random number
        :param int n: how many digits you want
        :return: n digit random number
        :rtype: int
    """
    range_start = 10 ** (n-1)
    range_end = (10 **n) -1
    return randrange(range_start, range_end)
