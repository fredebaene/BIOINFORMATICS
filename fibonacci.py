def calculate_number_of_rabbit_pairs_ONE(n, k):

    # n IS THE n-th MONTH FOR WHICH THE NUMBER OF RABBIT PAIRS IS CALCULATED
    # k IS THE NUMBER OF RABBIT PAIRS EACH RABBIT PAIR GETS AS OFFSPRING

    if n > 40 or k > 5:
        error_message = "Input restrictions : n can be no more than 40 and k no more than 5."
        return error_message

    A = [1, 0]
    B = [0, 0]

    if n < 3:
        number_of_rabbit_pairs = 1
        return number_of_rabbit_pairs
    else:
        for i in range(n - 1):
            B[0] = A[1] * k
            B[1] = sum(A)
            for j in range(len(A)):
                A[j] = B[j]
                B[j] = 0
        number_of_rabbit_pairs = sum(A)
        return number_of_rabbit_pairs

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

def probability_dominant_allele(k, m, n):
    
    # CALCULATING THE PROBABILITY THAT A CERTAIN COMBINATION WILL PRODUCE AN OFFSPRING WITH A DOMINANT ALLELE
    k_k = 1
    k_m = 1
    k_n = 1
    m_m = 0.75
    m_n = 0.5
    n_n = 0

    # CALCULATING THE TOTAL NUMBER OF CONSIDERED ORGANISMS
    total = k + m + n

    # CALCULATING THE PROBABILITY A CERTAIN COMBINATION WILL OCCURR AND PRODUCE AN OFSSPRING WITH A DOMINANT ALLELE
    prob_k_k = (k / total) * ((k - 1) / (total - 1)) * k_k
    prob_k_m = (((k / total) * (m / (total - 1))) + ((m / total) * (k / (total - 1)))) * k_m
    prob_k_n = (((k / total) * (n / (total - 1))) + ((n / total) * (k / (total - 1)))) * k_n
    prob_m_m = (m / total) * ((m - 1) / (total - 1)) * m_m
    prob_m_n = (((m / total) * (n / (total - 1))) + ((n / total) * (m / (total - 1)))) * m_n
    prob_n_n = (n / total) * ((n - 1) / (total - 1)) * n_n

    # CALCULATING THE OVERALL PROBABILITY
    probability = round(prob_k_k + prob_k_m + prob_k_n + prob_m_m + prob_m_n + prob_n_n, 5)

    return probability