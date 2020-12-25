from bioinformatics_toolkit import dna
from bioinformatics_toolkit import fasta_file_handling
from bioinformatics_toolkit import probability as prob

sequence = dna.DNA("ATTGTC")
premrna = sequence.transcribe_as_coding_strand()

print(sequence)
print(sequence.length)
print(premrna)
