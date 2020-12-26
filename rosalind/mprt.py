# ROSALIND INFORMATION - ID : MPRT - TITLE : FINDING A PROTEIN MOTIF

from bs4 import BeautifulSoup as bes
import requests

def get_protein_ids(file_directory):

    with open(file_directory, "r") as f:

        protein_list = f.readlines()
        protein_ids = []
        
        for i in range(len(protein_list)):

            if i == len(protein_list) - 1:
                protein_ids.append(protein_list[i])
            else:
                protein_ids.append(protein_list[i][:-1])

    return protein_ids

def get_protein_sequences(protein_ids):

    proteins = {}

    for i in protein_ids:

        link = "https://www.uniprot.org/uniprot/" + i + ".fasta"
        
        html_text = requests.get(link).text
        html_text_list = html_text.split("\n")
        protein_sequence = ""

        for j in html_text_list:

            if not len(j) == 0:

                if not j[0] == ">":

                    protein_sequence += j

        proteins[i] = protein_sequence

    return proteins

def locate_motifs(proteins):

    # N-GLYCOSYLATION MOTIF : N{P}[ST]{P}

    proteins_positions = {}
    
    for i in list(proteins):

        positions = []
        protein_sequence = proteins[i]
        protein_length = len(protein_sequence)
        last_possible_position = protein_length - (4 - 1)

        for j in range(last_possible_position):

            if (protein_sequence[j] == "N") and (not protein_sequence[j + 1] == "P") and (protein_sequence[j + 2] == "S" or protein_sequence[j + 2] == "T") and (not protein_sequence[j + 3] == "P"):

                positions.append(j + 1)

        if not len(positions) == 0:

            proteins_positions[i] = positions

    for i in list(proteins_positions):

        message = ""
        
        for j in proteins_positions[i]:

            message += str(j) + " "

        message = message[:-1]
            
        print(i)
        print(message)

if __name__ == "__main__":

    file = input("Please enter the file name : ")
    protein_ids = get_protein_ids(file)
    protein_sequences = get_protein_sequences(protein_ids)
    locate_motifs(protein_sequences)