# IMPORTING LIBRARIES
# ----------------------------------------------------------------------------------------------------
import pandas as pd
import os

# SEQUENCE CLASS
# ----------------------------------------------------------------------------------------------------
class Sequence(object):

    monomers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, sequence, label = None, description = None):

        for i in sequence:
            if i not in self.monomers:
                raise ValueError('Invalid Sequence')

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

        output = ''

        for i in self.monomers:
            output += str(occurrences[i]) + ' '

        return output[:-1]

    @classmethod
    def fasta(cls, file):

        if os.path.exists(file) == False:
            return 'Invalid File Path'

        data = pd.read_csv(file, header = None)
        end = pd.Series(['END'], name = 'end')
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

    def content(self, list_of_monomers):

        if not isinstance(list_of_monomers, list):
            return 'Invalid Object Type (list_of_monomers = List Object)'

        for i in list_of_monomers:
            if not i in self.monomers:
                return 'Invalid Monomers'

        numerator = 0

        for i in self.sequence:
            if i in list_of_monomers:
                numerator += 1

        return numerator / self.length

    @classmethod
    def overlap_start_index(cls, seq1, seq2):

        if not isinstance(seq1, cls) or not isinstance(seq2, cls):
            return 'Invalid Arguments : Sequence Objects Required'

        for i in range((seq1.length // 2) + (seq1.length % 2)):
            if seq2.sequence.startswith(seq1.sequence[i:]) == True and len(seq1.sequence[i:]) > seq2.length // 2:
                return i
        else:
            return -1

# DNA CLASS
# ----------------------------------------------------------------------------------------------------
class DNA(Sequence):

    monomers = 'ACGT'

    def transcribe_as_coding_strand(self):

        rna_sequence = ''

        for i in self.sequence:
            if i != 'T':
                rna_sequence += i
            else:
                rna_sequence += 'U'

        return RNA(sequence = rna_sequence)

    def reverse_complement(self):

        complementary_bases = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
        reverse_complement = ''

        for i in self.sequence[::-1]:
            reverse_complement += complementary_bases[i]

        return DNA(sequence = reverse_complement)

    @property
    def gc_content(self):
        return self.content(list_of_monomers = ['C', 'G'])

# RNA CLASS
# ----------------------------------------------------------------------------------------------------
class RNA(Sequence):

    monomers = 'ACGU'
