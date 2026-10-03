from modulefiles import calc_hamming_distance

with open("data/rosalind_hamm.txt", "r") as f:
    raw = f.read()

# test
# raw = """
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# """

seq_list = raw.strip().splitlines()
print(calc_hamming_distance(seq_list[0], seq_list[1]))