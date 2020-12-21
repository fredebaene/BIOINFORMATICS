from bioinformatics_toolkit import dna
from bioinformatics_toolkit import fasta_file_handling

ffd = "fasta.txt"

result = dna.find_shared_motif(ffd)
print(result)