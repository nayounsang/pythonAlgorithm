P = 53  # recommend prime
R = 10 ** 9 + 7  # recommend prine


def initHash(S, N, index):
    power = [1] * N
    for i in range(1, N):
        power[i] = (power[i - 1] * P) % R
    rabin = [0] * N
    rabin[0] = index[S[0]] * P
    for i in range(1, N):
        rabin[i] = ((rabin[i - 1] * P) % R + index[S[i]] * P) % R
    return power, rabin


rabin, power = initHash('abc', 3, {'a': 1, 'b': 2, 'c': 3})


def getHash(l, r):
    return (((R + rabin[r] - (rabin[l - 1] if l - 1 > 0 else 0)) % R) * power[r-l+1]) % R
