# ROSALIND INFORMATION - ID : REVC - TITLE : COMPLEMENTING A STRAND OF DNA
# ----------------------------------------------------------------------------------------------------

# IMPORING LIBRARIES
# ----------------------------------------------------------------------------------------------------
from bioinformatics import sequence as sq

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    sequence = input('Please enter your sequence : ')
    seq_1 = sq.DNA(sequence = sequence)
    revc = seq_1.reverse_complement()
    print(revc.sequence)
