# ROSALIND INFORMATION - ID : PMCH - TITLE : PERFECT MATCHINGS AND RNA SECONDARY STRUCTURES
# ----------------------------------------------------------------------------------------------------

# IMPORING LIBRARIES
# ----------------------------------------------------------------------------------------------------
from bioinformatics import sequence as sq

# DEFINITIONS
# ----------------------------------------------------------------------------------------------------
def fib(n):
    if n == 0:
        return 1
    else:
        return n * fib(n - 1)

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    file = input('Please enter the file path of the FASTA file : ')
    sequences = sq.RNA.fasta(file)
    a_u = int(sequences[0].monomer_occurrences().split(' ')[0])
    c_g = int(sequences[0].monomer_occurrences().split(' ')[1])
    result = fib(a_u) * fib(c_g)
    print(str(result))
