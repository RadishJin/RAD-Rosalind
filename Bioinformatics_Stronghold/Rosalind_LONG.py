from modulefiles.parse import parse_rosalind_fasta
from modulefiles.concat_shortest import concat_shortest

from itertools import combinations

# with open("data/rosalind_long.txt", "rt", encoding= "utf-8") as f:
#     raw = f.read()

raw = """
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
"""

seq_dict = parse_rosalind_fasta(raw)

# print(seq_tuples)

seq_list = list(seq_dict.values())
while True:

    concat_list = []
    seq_tuples = list(combinations(seq_list, 2))

    for seq1, seq2 in seq_tuples:
        concat_list.append(concat_shortest(seq1, seq2))

    concat_dict = dict(concat_list)
    # print(concat_dict)

    max_concat = max(concat_dict.items(), key = lambda x: x[1])
    max_concat = max_concat[0]

    pre_del = []
    for seq in seq_list:
        if seq in max_concat:
            pre_del.append(seq)

    seq_list.append(max_concat[0])

    for pre in pre_del:
        seq_list.remove(pre)

    if len(seq_list) == 1:
        break

print(seq_list[0][0])




        

