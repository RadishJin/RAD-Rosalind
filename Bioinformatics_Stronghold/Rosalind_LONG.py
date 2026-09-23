
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
seq_list = []
current = ""
for line in raw_list:
    if not line:
        continue
    if line.startswith(">"):
        continue
    else:
        seq_list.append(line)
print(seq_list)



        

