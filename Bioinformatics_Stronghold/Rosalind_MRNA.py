from Bio.Data import CodonTable
from collections import Counter

with open("data/rosalind_mrna.txt", "r") as f:
    seq = list(f.read().strip())

# raw = "MA"
# seq = list(raw)

def modulo(sequence: list) -> int:
    nmG = 3
    codon_table = CodonTable.unambiguous_dna_by_id[1]
    count = dict(Counter(codon_table.forward_table.values()))
    for i in sequence:
        nmG = (nmG * count[i]) % 1000000
    return nmG

print(modulo(seq))

