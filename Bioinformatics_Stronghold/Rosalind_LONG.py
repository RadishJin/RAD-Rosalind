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

raw_list = raw.strip().splitlines()
seq_dict = {}
current = ""
for line in raw_list:
    if not line:
        continue
    if line.startswith(">"):
        current = line[1:]
        seq_dict[current] = ""
    else:
        seq_dict[current] += line
# print(seq_dict)

