import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check if n is divisible by 2 or 3 (except for 2 and 3 themselves)
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for divisors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


# Example usage:
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
