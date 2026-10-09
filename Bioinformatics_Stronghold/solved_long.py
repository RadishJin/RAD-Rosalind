from modulefiles import parse_rosalind_fasta
from modulefiles import concat_shortest

from itertools import combinations

with open("data/rosalind_long.txt", "rt", encoding= "utf-8") as f:
    raw = f.read()

# raw = """
# >Rosalind_56
# ATTAGACCTG
# >Rosalind_57
# CCTGCCGGAA
# >Rosalind_58
# AGACCTGCCG
# >Rosalind_59
# GCCGGAATAC
# """

seq_dict = parse_rosalind_fasta(raw)

# print(seq_tuples)

seq_list = list(seq_dict.values())
while len(seq_list) > 1:
    max_overlap = -1
    best_merged = ""
    target_pair = None

    for seq1, seq2 in combinations(seq_list, 2):
        merged, overlap_len = concat_shortest(seq1, seq2)

        if overlap_len > max_overlap:
            max_overlap = overlap_len
            best_merged = merged
            target_pair = (seq1, seq2)

    if target_pair:
        s1, s2 = target_pair
        seq_list.remove(s1)
        seq_list.remove(s2)
        seq_list.append(best_merged)

print(seq_list[0])