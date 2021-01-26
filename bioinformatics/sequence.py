# IMPORTING LIBRARIES
# ----------------------------------------------------------------------------------------------------
import pandas as pd
import os

# SEQUENCE CLASS
# ----------------------------------------------------------------------------------------------------
class Sequence(object):

    monomers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, sequence, label = '', description = ''):

        for i in sequence:
            if i not in self.monomers:
                raise ValueError("Invalid Sequence")

        self.sequence = sequence
        self.label = label
        self.description = description

    @property
    def length(self):
        return len(self.sequence)

    def monomer_occurrences(self):

        occurrences = {}

        for i in self.monomers:
            occurrences[i] = 0

        for i in self.sequence:
            occurrences[i] += 1

        output = ""

        for i in self.monomers:
            output += str(occurrences[i]) + " "

        return output[:-1]

    @classmethod
    def fasta(cls, file):

        if not os.path.exists(file) == True:
            raise ValueError("Invalid File Path")

        data = pd.read_csv(file, header = None)
        end = pd.Series(['END'])
        fasta = data[0].append(end, ignore_index = True)
        sequences = []
        sequence, label, description = '', '', ''

        for i in range(len(fasta)):

            if fasta.iloc[i][0] == '>' or fasta.iloc[i] == 'END':

                if not i == 0:
                    sequences.append(cls(sequence = sequence, label = label, description = description))
                    sequence, label, description = '', '', ''

                if fasta.iloc[i] == 'END':
                    break

                else:
                    label_description = fasta.iloc[i].split(' ', 1)
                    if len(label_description) > 1:
                        label = label_description[0][1:]
                        description = label_description[1]
                    else:
                        label = label_description[0][1:]

            else:
                sequence += fasta.iloc[i]

        return sequences

# DNA CLASS
# ----------------------------------------------------------------------------------------------------
class DNA(Sequence):

    monomers = "ACGT"

    def transcribe_as_coding_strand(self):

        rna = ""

        for i in self.sequence:
            if i != "T":
                rna += i
            else:
                rna += "U"

        return RNA(rna)

    def reverse_complement(self):

        complementary_bases = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
        reverse_complement = ''

        for i in self.sequence[::-1]:
            reverse_complement += complementary_bases[i]

        return reverse_complement

# RNA CLASS
# ----------------------------------------------------------------------------------------------------
class RNA(Sequence):

    monomers = "ACGU"

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # ask user for sequence
    file = input("Please enter your sequence : ")
    sequences = DNA.fasta(file)

    # sequence analysis
    print(sequences)
