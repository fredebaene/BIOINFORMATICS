from dna import *
from fasta_handling import *

fasta_file_directory = "fasta_01.txt"

labeled_sequences = add_gc_content(read_fasta_file(fasta_file_directory))
output_highest_gc_content(labeled_sequences)