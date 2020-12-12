def validate_dna_sequence(sequence):
    
    max_length = 1000
    if len(sequence) > max_length:
        error_message = "Please enter a DNA sequence with a length of at most " + str(max_length) + " nucleotides."
        return error_message

    dna_nucleotides = ["A", "C", "G", "T"]
    
    for i in range(len(sequence)):
        if sequence[i].upper() not in dna_nucleotides:
            return False
    
    return True

def count_dna_nucleotides(sequence):

    if validate_dna_sequence(sequence) != True:
        error_message = "Please enter a valid DNA sequence."
        return error_message
    else:
        length_of_dna_sequence = len(sequence)
        return length_of_dna_sequence

def transcribe_dna_string(sequence):

    mapping_of_nucleotides = {"A" : "A", "C" : "C", "G" : "G", "T" : "U"}

    if validate_dna_sequence(sequence) != True:
        error_message = "Please enter a valid DNA sequence."
        return error_message
    else:
        rna_sequence = ""
        for i in range(len(sequence)):
            rna_sequence = rna_sequence + mapping_of_nucleotides[sequence[i]]
        return rna_sequence

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