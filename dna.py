"""
A DNA sequence is valid if and only if it contains zero or more of the following nucleotides :

    - ADENINE (A)
    - CYTOSINE (C)
    - GUANINE (G)
    - THYMINE (T)

The following function checks if the nucleotides in a given DNA sequence are no other than the ones mentioned above :

- if the sequence is valid, then the return value is TRUE
- if the sequence is not valid, then the return value is FALSE.
"""

def validate_sequence(sequence):

    dna_nucleotides = ["A", "C", "G", "T"]
    
    for i in range(len(sequence)):
        if sequence[i].upper() not in dna_nucleotides:
            return False
    
    return True

"""
The length of a DNA sequence is expressed as the number of nucleotides (or the number of base pairs). A base pair consists out of two nucleotides bonded together via its bases.

The following functionc calculates the length of a given DNA sequence if and only if the DNA sequence is valid. The return value of the function is an integer denoting the length of the DNA sequence expressed as the number of nucleotides.
"""

def calculate_sequence_length(sequence):

    if validate_sequence(sequence) != True:

        error_message = "Please enter a valid DNA sequence."
        return error_message

    else:

        length_of_sequence = len(sequence)
        return length_of_sequence

def calculate_nucleotide_occurrences(sequence):

    if validate_sequence(sequence) != True:

        error_message = "Please enter a valid DNA sequence."
        return error_message

    else:

        nucleotide_count = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}

        for i in range(len(sequence)):
            nucleotide_count[sequence[i].upper()] += 1

        return nucleotide_count

def output_nucleotide_occurrences(sequence):

    nucleotide_count = calculate_nucleotide_occurrences(sequence)
    output_message = str(nucleotide_count["A"]) + " " + str(nucleotide_count["C"]) + " " + str(nucleotide_count["G"]) + " " + str(nucleotide_count["T"])
    return print(output_message)

def transcribe_dna_sequence(sequence):

    mapping_of_nucleotides = {"A" : "A", "C" : "C", "G" : "G", "T" : "U"}

    if validate_dna_sequence(sequence) != True:
        error_message = "Please enter a valid DNA sequence."
        return error_message
    else:
        rna_sequence = ""
        for i in range(len(sequence)):
            rna_sequence = rna_sequence + mapping_of_nucleotides[sequence[i]]
        return rna_sequence