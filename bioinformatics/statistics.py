# STATISTICS CLASS
# ----------------------------------------------------------------------------------------------------
def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combinations(n, k):

    numerator = factorial(n)
    denominator = factorial(n - k) * factorial(k)
    combinations = numerator / denominator
    return combinations
