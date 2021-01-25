from bioinformatics_toolkit import fasta_file_handling

def overlap_graph(fasta_file_directory, k):

    labeled_sequences = fasta_file_handling.read_fasta_file(fasta_file_directory)
    sequence_overview = list(labeled_sequences)
    overlap_graph = []

    for i in range(len(sequence_overview)):

        if len(labeled_sequences[sequence_overview[i]][1]) < k:
            continue
        
        else:

            for j in range(len(labeled_sequences)):

                if len(labeled_sequences[sequence_overview[j]][1]) < k:
                    continue
                    
                elif labeled_sequences[sequence_overview[i]][1] == labeled_sequences[sequence_overview[j]][1]:
                    continue

                elif labeled_sequences[sequence_overview[i]][1][-k:] == labeled_sequences[sequence_overview[j]][1][0:k]:
                    overlap_graph.append([sequence_overview[i], sequence_overview[j]])
    
    return overlap_graph