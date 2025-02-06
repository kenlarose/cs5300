"""
Create an if statement to check if a given number is positive, negative, or zero. 
Implement a for loop to print the first 10 prime numbers 
(you may need to research how to calculate prime numbers). 
Create a while loop to find the sum of all numbers from 1 to 100.
Write pytest test cases to verify the correctness of your code for each control structure.
"""

def get_number_sign(number):
    if not isinstance(number, (int, float)):
        raise TypeError("argument must be a number")

    if (number > 0):
        return "positive"
    elif (number < 0):
        return "negative"
    else: 
        return "unsigned"


# hardcoding 10 since this can get computationally heavy at larger numbers
def first_ten_prime_numbers():
    prime_numbers = []
    number = 2

    while (len(prime_numbers) < 10):
        is_prime = True

        # non-primes will have a smaller prime factor
        for prime in prime_numbers:
            if number % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_numbers.append(number)

        number += 1
    
    return prime_numbers


def gauss_sum(n):
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer")  
    
    return (n * (n + 1)) // 2




    
    
