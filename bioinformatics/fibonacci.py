def calculate_number_of_rabbit_pairs_TWO(n, m):

    # n IS THE n-th MONTH FOR WHICH THE NUMBER OF RABBIT PAIRS IS CALCULATED
    # m IS THE NUMBER OF MONTHS EACH RABBIT LIVES

    if n > 100 or m > 20:
        error_message = "Input restrictions : n can be no more than 100 and m no more than 20."
        return error_message
    
    A = [1]
    B = [0]

    for i in range(m - 1):
        A.append(0)
        B.append(0)
    
    if n < 3:
        number_of_rabbit_pairs = 1
        return number_of_rabbit_pairs
    else:
        for i in range(n - 1):
            B[0] = sum(A[1:]) * 1
            for j in range(1, len(B)):
                B[j] = A[j - 1]
            for z in range(len(A)):
                A[z] = B[z]
                B[z] = 0
        number_of_rabbit_pairs = sum(A)
        return number_of_rabbit_pairs