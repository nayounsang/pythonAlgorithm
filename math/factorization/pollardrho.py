import math
import random


def power(x, y, r):
    # (x^y)%r
    result = 1
    x = x % r
    while y > 0:
        if y & 1:
            result = (result * x) % r
        y = y >> 1
        x = (x * x) % r
    return result


def millerRabin(ran, m, k, n):
    x = power(ran, m, n)
    if x == 1 or x == n - 1:
        return True
    for i in range(1, k):
        xx = (x ** 2) % n
        if xx == 1:
            return False
        elif xx == n - 1:
            return True
        x = xx
    return False


def isPrime(n):
    if n < 2 or not n & 1:
        return False
    if n == 2:
        return True
    m = n - 1
    k = 0
    while not m & 1:
        k += 1
        m = m >> 1
    alist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
    if n in alist:
        return True
    for a in alist:
        if a > n:
            break
        if not millerRabin(a, m, k, n):
            return False
    return True



def func(val, n, c):
    return ((val ** 2 % n) + c + n) % n


def pollardrho(n):
    if isPrime(n):
        return n
    if n == 1:
        return 1
    if not n & 1:
        return 2
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    while d == 1:
        x = func(x, n, c)
        y = func(func(y, n, c), n, c)
        d = math.gcd(abs(x - y), n)
        if d == n:
            return pollardrho(n)
    if isPrime(d):
        return d
    else:
        return pollardrho(d)


def factorization(n):
    result = []
    while n > 1:
        D = pollardrho(n)
        result.append(D)
        n = n // D
    return result
