# ROSALIND INFORMATION - ID : DNA - TITLE : COUNTING DNA NUCLEOTIDES
# ----------------------------------------------------------------------------------------------------

# IMPORING LIBRARIES
# ----------------------------------------------------------------------------------------------------
from bioinformatics import sequence as sq

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    sequence = input('Please enter your sequence : ')
    seq_1 = sq.DNA(sequence = sequence)
    print(seq_1.monomer_occurrences())
