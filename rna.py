# ROSALIND INFORMATION - ID : RNA - TITLE : TRANSCRIBING DNA INTO RNA
# ----------------------------------------------------------------------------------------------------

# IMPORING LIBRARIES
# ----------------------------------------------------------------------------------------------------
from bioinformatics import sequence as sq

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    sequence = input('Please enter your sequence : ')
    seq_1 = sq.DNA(sequence = sequence)
    rna_seq = seq_1.transcribe_as_coding_strand()
    print(rna_seq.sequence)
