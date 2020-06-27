"""
 Write a Python function that takes a number as a parameter and check the
number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that
has no positive divisors other than 1 and itself.
"""


def prime_check(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f'{num} is not prime')
                break
        else:
            print(f'{num} is prime')
    else:
        print(f'{num} is not prime')


inp = int(input("enter a number:"))
prime_check(inp)
