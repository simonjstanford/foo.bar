import math


def solution(n):
    prime_string = ''
    target_length = n + 5

    for p in primes_gen():
        prime_string += str(p)
        if len(prime_string) > target_length:
            break
    
    return prime_string[n:target_length]

def primes_gen():
    num = 1
    
    while True:
        num += 1
        if is_prime(num):
            yield num

def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    sq_root = int(math.sqrt(n))
    for i in range(2, sq_root + 1):
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    print(solution(0))
    print(solution(3))
