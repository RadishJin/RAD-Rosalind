from modulefiles import count_base

with open("data/rosalind_dna.txt", "r") as f:
    raw = f.read()

# testraw = """
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# """

seq_dict = count_base(raw)

for base in "ACGT":
    print(seq_dict.get(base, 0), end = " ")
    
