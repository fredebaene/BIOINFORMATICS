from bioinformatics_toolkit import dna
from bioinformatics_toolkit import fasta_file_handling
from bioinformatics_toolkit import probability as prob

sequence = "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"

mrna = dna.transcribe_dna_sequence(sequence)
print(sequence)
print(mrna)