def eulerphi(n):
    result = n
    fac = factorization(n)
    for f in fac:
        result = (result * f - result) // f
    return result