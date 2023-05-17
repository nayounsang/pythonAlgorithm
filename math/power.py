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
