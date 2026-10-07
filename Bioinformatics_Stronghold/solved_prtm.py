from modulefiles import calc_canonical_aa_monoiso_mass

with open("data/rosalind_prtm.txt", "r") as f:
    seq = list(f.read().strip())

# raw = "SKADYEK"

print(round(calc_canonical_aa_monoiso_mass(seq) - 18.010565, 3))


