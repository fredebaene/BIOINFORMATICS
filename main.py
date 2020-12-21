from dna import *
from fasta_handling import *

sequence_one = "ACGGCTAACCAAGCACGAAGGCGACGTCTTCTCCATTCTTCGAGTCTCACCTGAGGTACGGCTTTGCTTCACGGTAAATGTCGATTTTCTGTGTACCCACGGAACGCGACCAGGTACTCGCACCTTAGCTCCGGAACCGACCAATTTCCTCATTGAGCGTTTTGAACCAGTTATTACTTGCCGCTCAATGGAGACCACACGTTAGTTGAATCCCTCTACGTGTATATCTTGCCCGTATCCCGTCACGGTGTTACACGAGTATCCCAACCTAACTCAGAAACTGCCTAAGGAAAAATAGATCATCGGTCAGTTTGTATCTGATTTACTTCACCAAGACCTAACAACGTTTCCCTATCACTAGGCTGCCTGGTGGCTCTAGAAGTCGGACGATAGCATGCGGGTGCGTGTCCACGAAAGCGACTATCATAAGGTTACAAATTACGGGGAGTGATATCAAGAATTGCAACCTATGGTCTCGACGTATTGCTCCGGTCAGTGGGGCTGGGATCCATTAGGGTGAAGGTCGCGGCCACAATAGAAAGATGGGTCTATGACCGGGCCCGCGGTTTAGTCTAACAAAAACAGCGCCATAGTTTTTAGTCATCTAACCGGTACCTCTTAAAGTACACGCGCTGCGGTGTAAATCTAAACTCCTATTTTTGCTTTCGTCCTCCGGTGTGTGGCCATCCAGTTCCTCCCATACACGCCGACTGTGGGGCCCGGCAGTAGATCCACGCAGCGTTCAGCGCGCTAGACTCACATCGTGAGGAGTTCCGTCAGTCGCCTTACTTAGTCTAGTAAGGTAAACGATCACGGCACCGATGCACCTTATGATTGCATACATAACACTGATCCCTATTTATATACGTCCCCGATTCGCCGTTGGCCATCGAGCCAAAAGTGCATGAGTAGGGGATAGCTCTTTGCGTCGGATGATTATGGTGTACTCACACCTCCAACGTGA"
sequence_two = "ATTACGGTGCTAGCACCAAGACGATTCTCTGAAAAATCTGCTATAGACTCGACGTGTCGGGCTGGATGCCACCCTAAAAGAAAGCTGGCTTTGTACTTCCTGGGCACGAGTTGAGACGCTGGTCTTAGGACTGAAAGCGTCCGAGTCAGTCATGAGACCATCTGATCTTCTGATTCCTAGGTACTCTATCCTGACAGCACGTGCGTCGAGTTATAGTTCGGGTAGATGTGACTAGTGTTCGCTGCAAGCGTCATACTATATTGTTCCTCACCCCCAGAATTTACTGAGAGATAAAGCCCTAGCAGCCATTTCTGCACCCGTTATAGTTGGCTGATTGTATCCCACGGTTATACACGAGTGGGATACCTGGTTGCTCTACATTCGGTTCGAAGTGTTTCCGACCAGTGACCACTAAAATGGCTATGGTACGGTCGCAAAACAGGGCGAGTGATCTGACAGAATACTACCACGCGACTCTGCGTTGTTATCAGGTCTATGTAGCGCGGAACCGTTATGCCTAAAATTACACGCGCACCAGAAAAATGGGACAATTGGTCTACACTCGCATCTGCCACCCTTCATCAGCCGCAGGAAGTTTCGTAACGAATCCGGTGGCTCACAAAGATCATTGGGTAGGGTTTAAACCGGGACCTCTACATTAGACGAACTCGCCTGACGTGTAGGCGACCCAGCGCACAGAAGGACGTTGTCGGCGGGTCAACGCAGCGGCCGAAGTCCGCGGTCGCATGACTAGCTGGTCCACGCGAGTAAAGGGTCGGGTCGATGGACGCACGTCATTCACGACTACTTCCTCTGCGCTGGCATGATTTGACGTTCCACACATACCCGCCCCACCGTAAATAAAAGCGCCCGGGTGTTGACTGCGCCTTCAGCCCATTTATGTGTGAGAAGGGTACACCATGCGAAGTGGATTGCTTATGGTGCATCGTAGACGCTAACGATA"

hd = calculate_hamming_distance(sequence_one, sequence_two)
print(hd)