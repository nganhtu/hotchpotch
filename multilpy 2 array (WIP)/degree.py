def degree(coefficients):
    n = len(coefficients) - 1
    while n >= 0:
        if coefficients[n] != 0:
            return n
        n -= 1

    return 0
