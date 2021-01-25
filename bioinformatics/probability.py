import numpy as np

def probability_dominant_allele(k, m, n):
    
    # ROSALIND INFORMATION - TOPIC : PROBABILITY - ID : IPRB - TITLE : MENDLE'S FIRST LAW

    # THE PROBABILITY THAT A CERTAIN COMBINATION WILL PRODUCE AN OFFSPRING WITH A DOMINANT ALLELE
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

def independent_alleles(k, n):

    # ROSALIND INFORMATION - TOPIC : PROBABILITY - ID : LIA - TITLE : INDEPENDENT ALLELES

    """

    X is a random variable expressing the genotype of an offspring concerning the A/a-gene. Y is a random variable expressing the genotype of an offspring concerning the B/b-gene. Let event A equal X = Aa and event B equal Y = Bb.

    A FACTOR
    ---------
    (a) Both parents are of genotype Aa :
    
    X | A  | a
    -----------
    A | AA | Aa
    a | aA | aa
    
    P ( X = AA ) = 0.25
    P ( X = Aa ) = 0.5
    P ( X = aa ) = 0.25

    (b) One parent is of genotype Aa and the other of AA : 
    
    X | A  | A
    -----------
    A | AA | AA
    a | aA | aA

    P ( X = AA ) = 0.5
    P ( X = Aa ) = 0.5
    P ( X = aa ) = 0

    (c) One parent is of genotype Aa and the other of aa :

    X | a  | a
    -----------
    A | Aa | Aa
    a | aa | aa

    P ( X = AA ) = 0
    P ( x = Aa ) = 0.5
    P ( X = aa ) = 0.5

    Suppose a 3-tuple represents the following probability distribution : ( AA Aa aa ).

    F1 : ( 1/4 1/2 1/4 )                                -> ( 1/4 1/2 1/4 )
    F2 : ( 1/8 1/8 0 ) ( 1/8 1/4 1/8 ) ( 0 1/8 1/8 )    -> ( 1/4 1/2 1/4 )
    F3 : ...

    Suppose a 3-tuple represents the following probability distribution : ( BB Bb bb ) : ( 1/4 1/2 1/4 ).

    Suppose a 9-element matrix represents the following probability distribution :

    AABB AABb AAbb
    AaBB AaBb Aabb
    aaBB aaBb aabb.

    1/16 2/16 1/16
    2/16 4/16 2/16
    1/16 2/16 1/16    

    P ( X = Aa AND Y = Bb ) = 1/4

    Suppose : k = 2, N = 1. At least 1 out of 4 has genotype AaBb :
    
    - 1 out of 4 : (1/4)^1 * (3/4)^3 * (n CHOOSE k)
    - 2 out of 4 : (1/4)^2 * (3/4)^2 * (n CHOOSE k)
    - 3 out of 4 : (1/4)^3 * (3/4)^1 * (n CHOOSE k)
    - 4 out of 4 : (1/4)^4 * (3/4)^0 * (n CHOOSE k)

    """

    total_number = 2**k
    probability = 0

    for i in range(n, total_number + 1):
        
        probability += combinations(total_number, i) * (0.25)**i * (0.75)**(total_number - i)
    
    return probability

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combinations(n, k):
    
    numerator = factorial(n)
    denominator = factorial(n-k) * factorial(k)
    combinations = numerator / denominator
    return combinations

def matching_strings(sequence, probabilities):

    # ROSALIND INFORMATION - TOPIC : PROBABILITY - ID : PROB - TITLE : INTRODUCTION TO RANDOM STRINGS

    input_probabilities_list = probabilities.split(" ")
    probabilities_overview = {}
    output_probabilities_list = []

    for i in input_probabilities_list:

        probabilities_overview["G"] = round(float(i) / 2, 5)
        probabilities_overview["C"] = round(float(i) / 2, 5)
        probabilities_overview["A"] = round((1 - float(i)) / 2, 5)
        probabilities_overview["T"] = round((1 - float(i)) / 2, 5)

        probability = 1

        for j in range(len(sequence)):

            probability *= probabilities_overview[sequence[j]]
        
        output_probabilities_list.append(round(np.log10(probability), 3))
    
    return output_probabilities_list