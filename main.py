from bioinformatics_toolkit import dna
from bioinformatics_toolkit import fasta_file_handling
from bioinformatics_toolkit import probability as prob

k = 7
n = 37

result = round(prob.independent_alleles(k, n), 3)
print(result)