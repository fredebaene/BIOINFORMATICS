from bioinformatics_toolkit import dna

sequence = "TCTCGCCTTCATCTCGCCTCTCGCCTCTCGCCGTAGAGTTCTCGCCAGGGACGATCTCGCCTCTCGCCTTCTCGCCTCTCGCCGACTCTCGCCAGCGATTATCTCGCCGGGACGCTCTCGCCTCTCGCCCTTCTCTCTCGCCTCTCGCCGCGCGTGCTCTCGCCATATCTCGCCTCTCGCCGACCTCTCGCCCACTCTCGCCTGTTTTCTCGCCATACTCTCGCCTCTCGCCGATCTCGCCATCTCGCCGTCTCGCCGCATCTCGCCTCTCGCCTATCTCGCCTCGTCTCGCCTCTCGCCGTGGTTCTCGCCTGGCATCTCGCCGAGGCGATCTCGCCTCTCGCCATTCTCGCCCTCTCGCCAGAAACTCTCGCCGTCTCGCCTAGGGGTTCTCGCCTCTCGCCATGAGGGAGTCTCGCCTCTACTCATCTCGCCAGACTCTCGCCTCTCGCCGACGGTCTCGCCGATCTCGCCGAATCTCGCCCGTACTAGAATCTCGCCTCTCGCCTCTCGCCATCTCGCCCCTTCTCTCGCCTTCTCGCCCATCTCGCCCTCTCGCCTCTCGCCACTCTCGCCCTTCTCGCCGGTCTCGCCATTCTCGCCTCTCGCCCAGAACCATTCTCGCCGCTCTCGCCTCTCGCCGTCTCGCCGTCTCGCCGTCTCGCCTCTCGCCTCGTCCAACTCTCGCCTCTCGCCATCTCGCCATGAGTCTCTCGCCTCTCGCCCTATCTCGCCTCTCGCCTCATCTCTCGCCTCTCGCCACCTCTCGCCCGTCTCGCCGTCTTCTCGCCCTGCTTCTCGCCTCTCTCGCCTCTCGCCCATCTCGCCTCTCGCCATTTCTCGCCGTCTCGCCGTCTCGCCTCTCGCCTCTCGCCCTTCTCGCCAGATCTCGCCCAATCTCGCCGCCTACCGTCTCTCTCGCCGATCTCGCCGGTCTCGCCATTCTCGCCCATCTCGCCG"
motif = "TCTCGCCTC"

result = dna.find_motif_in_sequence(sequence, motif)
print(result)

output_result = ""

for i in range(len(result)):
    if i == 0:
        output_result = str(result[i])
    else:
        output_result += " " + str(result[i])

print(output_result)