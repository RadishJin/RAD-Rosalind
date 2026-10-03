from Bio.Seq import Seq

with open("data/rosalind_prot.txt", "r") as f:
    seq = f.read().strip()

# seq = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

prot = Seq.translate(seq,stop_symbol = "")
print(prot)
