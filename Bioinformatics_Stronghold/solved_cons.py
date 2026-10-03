from modulefiles import parse_rosalind_fasta, calc_profile, find_consensus

import numpy as np


with open("data/rosalind_cons.txt", "r") as f:
    raw = f.read()

# raw = """
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT
# """

seq_dict = parse_rosalind_fasta(raw)
seq_list = list(seq_dict.values())
base_list = [list(i) for i in seq_list]
base_matrix = np.vstack(base_list)

base = np.array(['A', 'C', 'G', 'T'])

profile = calc_profile(base_matrix)
consensus_seq = find_consensus(base_matrix)

print(consensus_seq)
for b, counts in zip(base, profile):
    print(f"{b}: {' '.join(map(str, counts))}")