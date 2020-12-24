from bioinformatics_toolkit import fasta_file_handling
import numpy as np

def validate_sequence(sequence):
    
    dna_nucleotides = ["A", "C", "G", "T"]
    
    for i in range(len(sequence)):
        if sequence[i].upper() not in dna_nucleotides:
            return False
    
    return True

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

    if validate_sequence(sequence) != True:
        
        error_message = "Please enter a valid DNA sequence."
        return error_message
    
    else:
        
        rna_sequence = ""
        
        for i in sequence:
            rna_sequence = rna_sequence + mapping_of_nucleotides[i]
        
        return rna_sequence
 
def calculate_gc_content(sequence):

     nucleotide_count = calculate_nucleotide_occurrences(sequence)
     gc_count = nucleotide_count["C"] + nucleotide_count["G"]
     total_count = nucleotide_count["A"] + nucleotide_count["C"] + nucleotide_count["G"] + nucleotide_count["T"]
     gc_content = round((gc_count / total_count) * 100, 6)
     return gc_content

def calculate_hamming_distance(sequence_a, sequence_b):

    hamming_distance = 0

    for i in range(len(sequence_a)):

        if sequence_a[i] != sequence_b[i]:
            hamming_distance += 1
    
    return hamming_distance

def translation(mrna_sequence):
    
    translation_dictionary = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V", "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V", "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A", "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E", "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G", "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"}

    codon_pos = 0
    number_of_codons = len(mrna_sequence) // 3
    protein = ""

    for i in range(number_of_codons):
        codon = mrna_sequence[codon_pos:codon_pos + 3]
        if translation_dictionary[codon] == "Stop":
            return protein
        else:
            protein += translation_dictionary[codon]
            codon_pos += 3
    
    return protein

def find_motif_in_sequence(sequence, motif):

    if validate_sequence(sequence) != True or validate_sequence(motif) != True:

        error_message = "Please enter a valid DNA sequence."
        return error_message
    
    elif len(motif) > len(sequence):
        
        error_message = "The motif length cannot be greater than the sequence length."
        return error_message
    
    else:
        
        positions = []
        end = len(sequence) - len(motif) + 1

        for i in range(end):

            if sequence[i:i + len(motif)] == motif:
                positions.append(i + 1)
        
        return positions

def find_profile_and_consensus(fasta_file_directory):

    sequences = fasta_file_handling.read_fasta_file(fasta_file_directory)

    sequence_overview = list(sequences)

    sequences_array = np.zeros((len(sequences), len(sequences[list(sequences)[0]][1])), dtype = "U1")
    profile = np.zeros((4, len(sequences[list(sequences)[0]][1])), dtype = "int32")
    nucleotides = ["A", "C", "G", "T"]
    consensus_string = ""

    for i in range(len(sequence_overview)):
        for j in range(len(sequences[sequence_overview[i]][1])):
            sequences_array[i, j] = sequences[sequence_overview[i]][1][j]

    for i in range(len(sequences_array)):
        for j in range(len(sequences_array[0, :])):
            profile[nucleotides.index(sequences_array[i, j]), j] += 1

    for j in range(len(sequences_array[0, :])):
        
        result = np.where(profile[:, j] == max(profile[:, j]))
        consensus_string += nucleotides[result[0][0]]

    result = [consensus_string, profile]

    return result

def output_find_consensus_and_profile(fasta_file_directory):

    result = find_profile_and_consensus(fasta_file_directory)
    nucleotides = ["A", "C", "G", "T"]
    message = result[0]

    for i in range(len(nucleotides)):
        
        message += "\n"
        message += nucleotides[i] + ":"
        
        for j in range(len(result[1][0, :])):
            message += " " + str(result[1][i, j])

    print(message)

def find_shared_motif(fasta_file_directory):

    sequences = fasta_file_handling.read_fasta_file(fasta_file_directory)
    sequence_overview = list(sequences)
    base_sequence = ""
    base_sequence_index = 0
    base_sequence_length = 0

    for i in range(len(sequence_overview)):
        
        if i == 0:
            base_sequence = sequences[sequence_overview[i]][1]
            base_sequence_index = i
            base_sequence_length = len(base_sequence)
       
        else:

            if len(sequences[sequence_overview[i]][1]) < base_sequence_length:
                base_sequence = sequences[sequence_overview[i]][1]
                base_sequence_index = i
                base_sequence_length = len(base_sequence)
    
    number_of_lengths = len(base_sequence) - 1
    subsequences = []

    for i in range(number_of_lengths):
        
        if len(subsequences) > 0:

            return subsequences
       
        else:

            subseq_length = base_sequence_length - i

            for j in range(base_sequence_length - subseq_length + 1):
                subsequence = base_sequence[j: j + subseq_length]
                included = True
                
                for k in range(len(sequence_overview)):
                    if not subsequence in sequences[sequence_overview[k]][1]:
                        included = False

                if included == True:
                    subsequences.append(subsequence)
            
            if included == True:
                return subsequences

    error_message = "There is no common motif."
    return error_message