from modulefiles import parse_rosalind_fasta, concat_custom
from itertools import permutations


with open("data/rosalind_grph.txt", "r") as f:
    raw = f.read()

# raw = """
# >Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG
# """

# data = raw.strip().splitlines()

seq_dict = parse_rosalind_fasta(raw)

for id1, id2 in permutations(seq_dict.keys(), 2):
    concat = concat_custom(seq_dict[id1], seq_dict[id2], 3)
    if concat != "":
        print(f"{id1} {id2}")
