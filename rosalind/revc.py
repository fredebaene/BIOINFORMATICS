# ROSALIND INFORMATION - ID : REVC - TITLE : COMPLEMENTING A STRAND OF DNA

def reverse_complement(sequence):

    mapping = {"A" : "T", "C" : "G", "G" : "C", "T" : "A"}
    reverse_sequence = sequence[::-1]
    reverse_complement = ""

    for i in reverse_sequence:

        reverse_complement += mapping[i]
    
    return reverse_complement


if __name__ == "__main__":

    sequence = input("Please enter your DNA sequence : ")
    reverse_complement = reverse_complement(sequence)
    print(reverse_complement)