# ROSALIND INFORMATION - ID : FIB - TITLE : RABBITS AND RECURRENCE RELATIONS

def calculate_number_of_rabbit_pairs_ONE(n, k):

    # n IS THE n-th MONTH FOR WHICH THE NUMBER OF RABBIT PAIRS IS CALCULATED
    # k IS THE NUMBER OF RABBIT PAIRS EACH RABBIT PAIR GETS AS OFFSPRING

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

if __name__ == "__main__":

    arguments = input("Please enter your arguments : ")
    n, k = arguments.split(" ")
    number_of_rabbit_pairs = calculate_number_of_rabbit_pairs_ONE(int(n), int(k))
    print(number_of_rabbit_pairs)