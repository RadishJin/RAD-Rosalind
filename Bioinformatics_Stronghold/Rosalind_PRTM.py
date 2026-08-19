from Bio.Data import IUPACData

with open("data/rosalind_prtm.txt", "r") as f:
    seq = list(f.read().strip())

# raw = "SKADYEK"
# seq = list(raw)

def molar_mass(sequence: list) -> float:
    mass = sum(IUPACData.monoisotopic_protein_weights[i] for i in sequence)
    dehydration = (len(sequence)) * 18.010565
    return mass - dehydration

print(molar_mass(seq))


