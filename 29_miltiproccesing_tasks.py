import concurrent.futures
import math
from multiprocessing import freeze_support
import os

print("Task 1======================================")
PRIMES = [
    1122725309293,
    1125870545678,
    1134567890011,
    1156798342456,
    1099726899875
]

def is_prime(n):
    print(f"{n} is counted on procces")
    if n <2:
        return False
    if n ==2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n +1, 2):
        if n%i ==0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor()  as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('% is prime: %s' % (number, prime))

if __name__ == '__main__':
    freeze_support()
    main()

