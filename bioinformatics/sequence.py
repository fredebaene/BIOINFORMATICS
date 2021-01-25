# SEQUENCE CLASS
# ----------------------------------------------------------------------------------------------------
class Sequence(object): # a class is a blueprint describing the objects belonging to that class

    elements = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # class variables are shared among all instances of the class
    sequence_type = "sequence"

    def __init__(self, sequence): # the init method can also be considered as a constructor method
        self.sequence = sequence # attributes are instance variables

    def print_sequence(self): # a method inside of a class automatically takes the instance as its first argument
        return self.sequence

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    
    seqOne = Sequence("ATATCGG") # the init method is run automatically whenever a new instance of a class is created
    seqTwo = Sequence("TATCGGTATCGCGCG")

    for i in Sequence.elements:
        print(i)
