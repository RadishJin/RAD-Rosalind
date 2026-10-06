from modulefiles import parse_rosalind_fasta, find_only_motif

with open("data/rosalind_lcsm.txt", "r") as f:
    raw = f.read()

# raw = """
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA
# """

seq_list = list(parse_rosalind_fasta(raw).values())
print(find_only_motif(seq_list))
    
