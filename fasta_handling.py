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
                sequence += fasta[i][:-1]
        
        labeled_sequences[label] = [description, sequence]
    
    return labeled_sequences