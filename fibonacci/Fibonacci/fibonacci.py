def generate_fibonacci(n):
    """
    Generate fibonacci sequence to n place
    """
    fibonacci = []
    for i in range(n + 1):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    return fibonacci
            
def main():
    """
    Testing
    """
    for i in range(19):
        print generate_fibonacci(i)

if __name__ == "__main__":
    main()    
