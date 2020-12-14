def calculate_number_of_rabbit_pairs_ONE(n, k):

    # n IS THE n-th MONTH FOR WHICH THE NUMBER OF RABBIT PAIRS IS CALCULATED
    # k IS THE NUMBER OF RABBIT PAIRS EACH RABBIT PAIR GETS AS OFFSPRING

    if n > 40 or k > 5:
        error_message = "Input restrictions : n can be no more than 40 and k no more than 5."
        return error_message

    A = [1, 0]
    B = [0, 0]

    if n < 3:
        number_of_rabbit_pairs = 1
        return number_of_rabbit_pairs
    else:
        for i in range(n - 1):
            B[0] = A[1] * k
            B[1] = sum(A)
            for j in range(len(A)):
                A[j] = B[j]
                B[j] = 0
        number_of_rabbit_pairs = sum(A)
        return number_of_rabbit_pairs

def calculate_number_of_rabbit_pairs_TWO(n, m):

    # n IS THE n-th MONTH FOR WHICH THE NUMBER OF RABBIT PAIRS IS CALCULATED
    # m IS THE NUMBER OF MONTHS EACH RABBIT LIVES

    if n > 100 or m > 20:
        error_message = "Input restrictions : n can be no more than 100 and m no more than 20."
        return error_message
    
    A = [1]
    B = [0]

    for i in range(m - 1):
        A.append(0)
        B.append(0)
    
    if n < 3:
        number_of_rabbit_pairs = 1
        return number_of_rabbit_pairs
    else:
        for i in range(n - 1):
            B[0] = sum(A[1:]) * 1
            for j in range(1, len(B)):
                B[j] = A[j - 1]
            for z in range(len(A)):
                A[z] = B[z]
                B[z] = 0
        number_of_rabbit_pairs = sum(A)
        return number_of_rabbit_pairs

def calculate_gc_content(sequence):

    nucleotide_count = calculate_nucleotide_occurences(sequence)

    gc_count = nucleotide_count["G"] + nucleotide_count["C"]
    total_count = len(sequence)
    gc_content = round((gc_count / total_count) * 100, 6)

    return gc_content

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
    
    return labeled_sequences