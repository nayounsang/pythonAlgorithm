"""
if n > 1 and n % 2 == 1:
    (n - 1) % 2 == 0
    n - 1 = (2 ^ k) * m (k > 1 and m % 2 == 1)
a = random(2,n-2)
b0 = (a ^ m) % n
if |b0| == 1:
    n is prime maybe...
for i in range(1,k):
    b(i) = (b(i-1)^2) % n
    if b(i) == 1:
        not prime
        break
    elif b(i) == -1:
        prime
        break
"""


def power(x, y, r): # 빠른 거듭제곱을 위함
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
