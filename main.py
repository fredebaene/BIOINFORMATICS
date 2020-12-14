from dna import *
from fasta_handling import *

fasta_file_directory = "fasta_01.txt"

labeled_sequences = read_fasta_file(fasta_file_directory)

print(labeled_sequences)