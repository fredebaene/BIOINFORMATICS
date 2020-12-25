# ROSALIND INFORMATION - ID : DNA - TITLE : COUNTING DNA NUCLEOTIDES

def calculate_nucleotide_occurrences(sequence):

    nucleotide_occurrences = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}

    for i in sequence:
        nucleotide_occurrences[i] += 1

    return nucleotide_occurrences

def print_nucleotide_occurrences(nucleotide_occurrences):

    message = str(nucleotide_occurrences["A"]) + " " + str(nucleotide_occurrences["C"]) + " " + str(nucleotide_occurrences["G"]) + " " + str(nucleotide_occurrences["T"])

    print(message)

if __name__ == "__main__":

    sequence = input("Please enter your DNA sequence : ")
    nucleotide_occurrences = calculate_nucleotide_occurrences(sequence)
    print_nucleotide_occurrences(nucleotide_occurrences)