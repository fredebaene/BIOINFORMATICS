# SEQUENCE CLASS
# ----------------------------------------------------------------------------------------------------
class Sequence(object):

    monomers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sequence_type = "sequence"

    def __init__(self, sequence):

        for i in sequence:
            if i not in self.monomers:
                raise ValueError("Invalid Sequence")

        self.sequence = sequence

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

# DNA CLASS
# ----------------------------------------------------------------------------------------------------
class DNA(Sequence):

    monomers = "ACGT"
    sequence_type = "DNA"

    def transcribe_as_coding_strand(self):

        rna = ""

        for i in self.sequence:
            if i != "T":
                rna += i
            else:
                rna += "U"

        return RNA(rna)

# RNA CLASS
# ----------------------------------------------------------------------------------------------------
class RNA(Sequence):

    monomers = "ACGU"
    sequence_type = "RNA"

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # ask user for sequence
    sequence = input("Please enter your sequence : ")

    # sequence analysis
    seqOne = DNA(sequence)
    seqTwo = seqOne.transcribe_as_coding_strand()
    print(type(seqTwo))
    print(seqTwo.sequence)
