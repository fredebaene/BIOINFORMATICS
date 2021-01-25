# SEQUENCE CLASS
# ----------------------------------------------------------------------------------------------------

class Sequence(object): # a class is a blueprint describing the objects belonging to that class

    def __init__(self, sequence):

        self.sequence = sequence # attributes are instance variables

# APPLICATION
# ----------------------------------------------------------------------------------------------------

seqOne = Sequence("ATATCGG") # the init method is run automatically whenever a new instance of a class is created
seqTwo = Sequence("TATCGGTATCGCGCG") # the init method is run automatically whenever a new instance of a class is created

print(seqOne)
print(seqTwo)
print(type(seqOne))
print(type(seqTwo))
print(seqOne.sequence)
print(seqTwo.sequence)
