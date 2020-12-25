# ROSALIND INFORMATION - ID : RNA - TITLE : TRANSCRIBING DNA INTO RNA

def transcribe_as_coding_strand(sequence):

    mapping = {"A" : "A", "C" : "C", "G" : "G", "T" : "U"}
    pre_mrna = ""

    for i in sequence:

        pre_mrna += mapping[i]
    
    return pre_mrna

if __name__ == "__main__":

    sequence = input("Please enter your DNA sequence : ")
    pre_mrna = transcribe_as_coding_strand(sequence)
    print(pre_mrna)