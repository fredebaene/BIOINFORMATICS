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