# ROSALIND INFORMATION - ID : LONG - TITLE : GENOME ASSEMBLY AS SHORTEST SUPERSTRING
# ----------------------------------------------------------------------------------------------------

# IMPORING LIBRARIES
# ----------------------------------------------------------------------------------------------------
from bioinformatics import sequence as sq

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    file = input('Please enter the file path of the FASTA file : ')
    starting_node = None
    tail_nodes = sq.DNA.fasta(file)
    head_nodes = []
    indexes = []

    for i in range(len(tail_nodes)):

        head_nodes.append(None)
        indexes.append(tail_nodes[i].length)

        for j in tail_nodes:

            if tail_nodes[i] != j:

                index = sq.DNA.overlap_start_index(tail_nodes[i], j)

                if index != -1 and index < indexes[i]:

                    head_nodes[i] = j
                    indexes[i] = index

    for i in range(len(tail_nodes)):
        if tail_nodes[i] not in head_nodes:
            starting_node = i

    run = True
    new_seq = ''

    while run == True:
        new_seq += tail_nodes[starting_node].sequence[:indexes[starting_node]]
        if not head_nodes[starting_node] == None:
            starting_node = tail_nodes.index(head_nodes[starting_node])
        else:
            run = False

    shortest_superstring = sq.DNA(sequence = new_seq)
    print(shortest_superstring.sequence)
