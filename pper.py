# ROSALIND INFORMATION - ID : PPER - TITLE : PARTIAL PERMUTATIONS
# ----------------------------------------------------------------------------------------------------

# IMPORING LIBRARIES
# ----------------------------------------------------------------------------------------------------
from bioinformatics import sequence as sq
from bioinformatics import statistics as stat

# APPLICATION
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    input = str(input('Please enter the data : '))
    n, k = input.split(' ', 1)
    combinations = stat.combinations(int(n), int(k))
    result = int((combinations * stat.factorial(int(k))) % 1000000)
    print(str(result))
