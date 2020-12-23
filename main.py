from bioinformatics_toolkit import dna
from bioinformatics_toolkit import fasta_file_handling


k = int(input("Enter the generation: "))
total_number = 2**k
print(total_number)
n = int(input("The mimimal number : "))
print(n)
probability = 0
pow = n

for i in range(n, total_number + 1):
    probability += ((0.25)**i) * ((0.75)**(total_number - i))

print(probability)