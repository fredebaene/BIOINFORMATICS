# IMPORTING LIBRARIES
# ----------------------------------------------------------------------------------------------------
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

        with open(file, 'r') as f:
            lines_of_text = f.readlines()

        lines_of_text.append('$\n')
        sequences = []
        label, description, sequence = '', '', ''

        for i in range(len(lines_of_text)):

            if lines_of_text[i][0] == '$':

                break

            elif lines_of_text[i + 1][0] == '>' or lines_of_text[i + 1][0] == '$':

                sequences.append(cls(sequence = sequence, label = label, description = description))
                label, description, sequence = '', '', ''

            elif lines_of_text[i][0] == '>':

                label_description = lines_of_text[i].split(' ', 1)

                if len(label_description) > 1:
                    label = label_description[0][1:]
                    description = label_description[1][:-1]
                else:
                    label = label_description[0][1:-1]

            else:

                sequence += lines_of_text[i][:-1]

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
    sequence = input("Please enter your sequence : ")

    seqOne = DNA(sequence = sequence)
    print(seqOne.reverse_complement())
