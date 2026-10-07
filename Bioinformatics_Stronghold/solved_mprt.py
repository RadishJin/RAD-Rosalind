from Bioinformatics_Stronghold.modulefiles import find_pattern
from modulefiles import parse_uniprot_fasta, io_uniprot_fasta


with open("data/rosalind_mprt.txt", "r") as f:
    raw = f.read()

# raw = """
# A2Z669
# B5ZC00
# P07204_TRBM_HUMAN
# P20840_SAG1_YEAST
# """



raw_ids = raw.strip().split("\n")
clean_ids = [i.split("_")[0] for i in raw_ids]

raw = io_uniprot_fasta(clean_ids)
for i in range(len(raw[1])):
    omit_idx = clean_ids.index(raw[1][i])
    raw_ids.remove(raw_ids[omit_idx])
    clean_ids.remove(raw[1][i])

prot_dict = parse_uniprot_fasta(raw[0])


motif_regex = r"(?=N[^P][ST][^P])"

locat_dict = {}
for id, prot in prot_dict.items():

    id_idx = list(prot_dict.keys()).index(id)
    full_id = raw_ids[id_idx]

    locat_dict[full_id] = list(map(lambda x: x + 1, find_pattern(motif_regex, prot, regex= True)))

for id in raw_ids:
    if id in locat_dict.keys():
        if locat_dict[id]:
            print(id)
            print(*locat_dict[id])


