def calculate_prime_factor(n):
    """
    :param int n: number to be prime factorized
    :return: list of prime factors
    :rtype: list
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    
def main():
    """
    Testing
    """
    print calculate_prime_factor(9)
    print calculate_prime_factor(56)
    print calculate_prime_factor(55)
    print calculate_prime_factor(54)
    print calculate_prime_factor(57)
    
if __name__ == "__main__":
    main()
