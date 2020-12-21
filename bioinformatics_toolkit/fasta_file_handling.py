from bioinformatics_toolkit import dna

def read_fasta_file(fasta_file_directory):

    with open(fasta_file_directory) as f:

        fasta = f.readlines()
        labeled_sequences = {}

        for i in range(len(fasta)):

            if fasta[i][0] == ">":
                
                if i > 0:
                    labeled_sequences[label] = [description, sequence]

                label = ""
                description = ""
                sequence = ""

                if fasta[i].count(" ") == 0:
                    label = fasta[i][1:-1]
                else:
                    label = fasta[i].split(" ", 1)[0][1:-1]
                    description = fasta[i].split(" ", 1)[1][:-1]
                
            else:

                    if i < len(fasta) - 1:
                        sequence += fasta[i][:-1]
                    else:
                        sequence += fasta[i]
        
        labeled_sequences[label] = [description, sequence]
    
    return labeled_sequences

def add_gc_content(labeled_sequences):

    for k, v in labeled_sequences.items():
        v.append(calculate_gc_content(v[1]))
    
    return labeled_sequences

def output_highest_gc_content(labeled_sequences):

    labels = []
    gc_contents = []

    for k, v in labeled_sequences.items():
        labels.append(k)
        gc_contents.append(v[2])

    return print(str(labels[gc_contents.index(max(gc_contents))]) + "\n" + str(max(gc_contents)))