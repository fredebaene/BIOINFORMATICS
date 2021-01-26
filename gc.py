# ROSALIND INFORMATION - ID : GC - TITLE : COMPUTING GC CONTENT
# ----------------------------------------------------------------------------------------------------

# IMPORING LIBRARIES
# ----------------------------------------------------------------------------------------------------
from bioinformatics import sequence as sq

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    file = input('Please enter the file path of the FASTA file : ')
    sequences = sq.DNA.fasta(file)
    index = 0
    ref_gc_content = 0
    for i in range(len(sequences)):
        if sequences[i].gc_content > ref_gc_content:
            index = i
            ref_gc_content = sequences[i].gc_content
    print(sequences[index].label)
    print(str(round(sequences[index].gc_content * 100, 6)))
